# open csv file and take only 20 records from it and save it as sample_data.csv


import pandas as pd

df =pd.read_csv("/home/bharath/fraud_detection_mlops/Synthetic_Financial_datasets_log.csv")
df = df.sample(20)

#save just like the original dataset
df.to_csv("/home/bharath/fraud_detection_mlops/tests/sample_data.csv", index=True)