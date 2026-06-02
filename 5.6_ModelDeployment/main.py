from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class InputData(BaseModel):
    hours: float

@app.post('/predict')
def predict(data: InputData):
    hours = np.array([[data.hours]])
    prediction = model.predict(hours)[0]
    return {"predicted_score": prediction}