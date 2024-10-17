import pytest
import numpy as np
import os 
from joblib import load, dump
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocess import preprocess_data
# from src.test import test_model

@pytest.fixture
def csv_path():
    dataset_path = "./tests/sample_data.csv"

    return dataset_path

def test_preprocess_data(csv_path):
    X_train, X_test, Y_train, Y_test = preprocess_data(csv_path)

    # check the shapes of the datasets
    assert X_train.shape[1] >4
    assert X_test.shape[1] >4
    assert Y_train.shape[0] > 0
    assert Y_test.shape[0] > 0



@pytest.fixture
def load_model():
    model = load("./tests/decision_tree_model.pkl")
    return model 


def test_model(load_model):
    assert load_model is not None


if __name__=="__main__":
    pytest.main(["-v",__file__])

