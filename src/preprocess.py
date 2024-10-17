# importing the library
# importing the library
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report, confusion_matrix

# read data

def preprocess_data(csv_path):
    df = pd.read_csv(csv_path)    
    df.drop(['oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest'], axis = 1, inplace = True)
    df.drop(['nameOrig', 'nameDest'], axis = 1, inplace = True)

    # encoding the categorical column into numerical data
    le = LabelEncoder()
    df['type'] = le.fit_transform(df['type'])

    # splitting the data into training and testing data
    X = df.drop('isFraud', axis = 1)
    y = df['isFraud']

    # standardizing the data
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    # splitting the data into training and testing data
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size = 0.3, random_state = 42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data("/home/bharath/fraud_detection_mlops/Synthetic_Financial_datasets_log.csv")
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    import ipdb;ipdb.set_trace()
    print(X_test[0])
    print(X_test[1])
    print(X_test[2])
