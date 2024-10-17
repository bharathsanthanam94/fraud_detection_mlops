'''
evaluate the trained  model for financial fraude detection

'''

import sys
import os
import numpy as np
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocess import preprocess_data
from src.train import train_model, evaluate_model
from joblib import load
# pass the test data sample to trained model and get the prediction
def test_model(model, X_test):
    X_test = np.array([X_test])
    y_pred = model.predict(X_test)
    return y_pred


if __name__ == "__main__":
    # create one random data sample for testing
    # X_test = [[0.24311303, -1.2696312 ,  0.24899309, -0.00158578]]
    # X_test = [[-1.60467997e+00,  9.52399323e-01, -2.78566769e-01, -1.58577857e-03]]
    X_test = [-1.63980912e+00, -1.26963120e+00, -4.57022763e-02, -1.58577857e-03]
    model = load("decision_tree_model.pkl")
    y_pred = test_model(model, X_test)
    print(y_pred)


# example test data
'''
[ 0.24311303 -1.2696312   0.24899309 -0.00158578]
[-1.60467997e+00  9.52399323e-01 -2.78566769e-01 -1.58577857e-03]
[-1.63980912e+00 -1.26963120e+00 -4.57022763e-02 -1.58577857e-03]
'''