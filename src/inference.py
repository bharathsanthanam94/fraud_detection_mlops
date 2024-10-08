import json
import joblib
from .test import test_model

def model_fn(model_dir):
    """Load the model from the model_dir."""
    model = joblib.load(f"{model_dir}/decision_tree_model.pkl")
    return model

def input_fn(request_body, request_content_type):
    """Parse input data payload."""
    if request_content_type == 'application/json':
        input_data = json.loads(request_body)
        return input_data['instances']
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    """Make prediction using the input data and loaded model."""
    return test_model(model, input_data)

def output_fn(prediction, response_content_type):
    """Format prediction output."""
    if response_content_type == 'application/json':
        return json.dumps(prediction.tolist())
    raise ValueError(f"Unsupported content type: {response_content_type}")