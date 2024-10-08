#!/bin/bash

# Set variables
AWS_ACCOUNT_ID="your-aws-account-id"
AWS_REGION="your-aws-region"
ECR_REPOSITORY="your-ecr-repository-name"
IMAGE_TAG="latest"

# Create ECR repository if it doesn't exist
aws ecr describe-repositories --repository-names "${ECR_REPOSITORY}" --region "${AWS_REGION}" || \
    aws ecr create-repository --repository-name "${ECR_REPOSITORY}" --region "${AWS_REGION}"

# Authenticate Docker to ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Build the Docker image
docker build -t $ECR_REPOSITORY:$IMAGE_TAG .



# Tag the image for SageMaker
docker tag $ECR_REPOSITORY:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG-sagemaker

# Push the SageMaker-tagged image to ECR
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG-sagemaker