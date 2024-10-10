# importing the library
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report, confusion_matrix
from preprocess import preprocess_data
import joblib
def train_model(X_train, X_test, y_train, y_test):
    # training the model with decision tree classification
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # save the model
    joblib.dump(model, 'decision_tree_model.pkl')
    return model

def evaluate_model(model, X_test, y_test):
    # predicting the test data
    y_pred = model.predict(X_test)

    # evaluating the model
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
    print(f"Recall: {recall}")
    
    # classification report
    print(classification_report(y_test, y_pred))

    # confusion matrix
    print(confusion_matrix(y_test, y_pred))
    return accuracy, recall, precision

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data("/home/bharath/fraud_detection/datasets/Synthetic_Financial_datasets_log.csv")

    model = train_model(X_train, X_test, y_train, y_test)
    # import ipdb;ipdb.set_trace()
    accuracy, recall, precision = evaluate_model(model, X_test, y_test)
