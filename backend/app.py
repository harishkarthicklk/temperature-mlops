from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "pkl_file",
    "current_model.pkl"
)

model = joblib.load(MODEL_PATH)
@app.get("/")
def home():
    return {"message": "Temperature Predictor API"}

@app.post("/predict")
def predict(data: dict):

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)

    return {
        "predicted_temperature": float(prediction[0])
    }