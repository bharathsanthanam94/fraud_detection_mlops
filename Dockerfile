# Use Python 3.10 slim-bullseye as the base image (smaller than slim)
FROM python:3.10-slim-bullseye as builder

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Install system dependencies and Poetry, then clean up in a single layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION} \
    && apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy only the files needed for installation
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy only the tests and src directories
COPY tests ./tests
COPY src ./src

# Create a new stage for the final image
FROM python:3.10-slim-bullseye as final

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app
COPY --from=builder /opt/poetry /opt/poetry

# Set the working directory
WORKDIR /app

# Set the PATH to include Poetry
ENV PATH="/opt/poetry/bin:$PATH"

# Set the entrypoint for SageMaker
ENTRYPOINT ["python", "src/inference.py"]

# Set the default command to run your application (this will be overridden by SageMaker)
# CMD ["poetry", "run", "python", "src/test.py"]
