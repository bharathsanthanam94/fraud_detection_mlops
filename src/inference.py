import os
import json
import joblib
import numpy as np

def model_fn(model_dir):
    """Load the model from the model_dir."""
    model_path = os.path.join(model_dir, "decision_tree_model.pkl")
    model = joblib.load(model_path)
    return model

def input_fn(request_body, request_content_type):
    """Parse input data payload."""
    if request_content_type == "application/json":
        input_data = json.loads(request_body)
        return np.array(input_data)
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    """Perform prediction on the deserialized data."""
    return model.predict(input_data)

def output_fn(prediction, accept):
    """Format prediction output."""
    if accept == "application/json":
        return json.dumps(prediction.tolist())
    raise ValueError(f"Unsupported accept type: {accept}")