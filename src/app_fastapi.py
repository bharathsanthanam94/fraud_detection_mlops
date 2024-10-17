from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
import numpy as np 
from joblib import load 


model = load("decision_tree_model.pkl")

app = FastAPI()

class TransactionFeatures(BaseModel):
	features: list[float]


@app.post("/predict")
async def predict_fraud(transaction: TransactionFeatures):
	try:
		X = np.array([transaction.features])
        prediction = model.predict(X)
        return {"prediction": int(prediction[0])}
    except Exception as e:
    	raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
	return {"message: Financial transaction fraud detection ML Model"}


if __name__=="__main__":
	import uvicorn
	uvicorn.run(app, host= "0.0.0.0", port=8000)