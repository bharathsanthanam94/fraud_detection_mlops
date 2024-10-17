# import sagemaker
# from sagemaker.model import Model
# import time
# def deploy_model_from_custom_ecr():
#     # Initialize SageMaker session
#     sagemaker_session = sagemaker.Session()

#     # Define the ECR image URI
#     account_id = sagemaker_session.account_id()
#     region = sagemaker_session.boto_region_name
#     image_uri = "010438480794.dkr.ecr.us-east-1.amazonaws.com/test_ml_demo:test_ml_image"
    
#      # Create a valid model name
#     model_name = f"fraud-detection-model-{int(time.time())}"
#     # Create Model object
#     model = Model(
#         image_uri=image_uri,
#         model_data="s3://fraud-detection-mode/model.tar.gz",
#         role=sagemaker.get_execution_role(),
#          name=model_name, 
#         sagemaker_session=sagemaker_session
#     )
#     print("image loaded")
#     # Deploy the model
#     predictor = model.deploy(
#         initial_instance_count=1,
#         instance_type="ml.t2.medium",
#         endpoint_name=f"fraud-detection-endpoint-{int(time.time())}"
#     )

#     print(f"Endpoint created: {predictor.endpoint_name}")

# if __name__ == "__main__":
#     deploy_model_from_custom_ecr()


import sagemaker
from sagemaker.sklearn.model import SKLearnModel
from sagemaker import get_execution_role
import boto3
import time
import numpy as np

def deploy_sklearn_model_from_s3(model_data):
    # Initialize SageMaker session
    sagemaker_session = sagemaker.Session()
    role = get_execution_role()

    # Create SKLearnModel object
    model = SKLearnModel(
        model_data=model_data,
        role=role,
        framework_version="0.23-1",  # Choose the appropriate scikit-learn version
        py_version="py3",
        sagemaker_session=sagemaker_session
    )

    # Generate a unique endpoint name
    endpoint_name = f"sklearn-endpoint-{int(time.time())}"

    # Deploy the model
    predictor = model.deploy(
        initial_instance_count=1,
        instance_type="ml.t2.medium",  # Choose an appropriate instance type
        endpoint_name=endpoint_name
    )

    print(f"Model deployed. Endpoint name: {endpoint_name}")

    return predictor

def test_endpoint(predictor):
    # Test data - adjust according to your model's input format
    test_data = np.array([[0.24311303, -1.2696312, 0.24899309, -0.00158578]])

    # Make a prediction
    result = predictor.predict(test_data)
    print(f"Prediction result: {result}")

if __name__ == "__main__":
    # S3 path to your existing model tar file
    model_data = "s3://fraud-detection-mode/model.tar.gz"

    # Deploy the model
    predictor = deploy_sklearn_model_from_s3(model_data)

    # Test the endpoint
    test_endpoint(predictor)