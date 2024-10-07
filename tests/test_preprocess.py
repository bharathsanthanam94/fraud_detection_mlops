import pytest
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocess import preprocess_data

def test_preprocess_data():
    X_train, X_test, y_train, y_test = preprocess_data("/home/bharath/fraud_detection/datasets/Synthetic_Financial_datasets_log.csv")
    assert X_train.shape[0] > 0
    assert X_test.shape[0] > 0
    assert y_train.shape[0] > 0
    assert y_test.shape[0] > 0

if __name__ == "__main__":
    pytest.main(["-v", __file__])

