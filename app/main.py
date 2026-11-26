from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import logging
from datetime import datetime
import numpy as np
from prometheus_client import Counter #nuevo
from fastapi.responses import Response #nuevo
from prometheus_client import generate_latest #nuevo



app = FastAPI()
#inicio nuevo
REQUEST_COUNT = Counter(
    "prediction_requests_total",
    "Total prediction requests"
)

DRIFT_COUNT = Counter(
    "prediction_drift_total",
    "Total drift detections"
)#fin nuevo

model = joblib.load("app/model.pkl")
baseline = joblib.load("app/baseline.pkl") #nuevo

prediction_count = 0
drift_count = 0 #nuevo

FEATURES = [    "age",    "sex",    "bmi",
    "bp",    "s1",    "s2",    "s3",
    "s4",    "s5",    "s6"
]


class PredictionRequest(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

logging.basicConfig(
    filename="predictions.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.get("/")
def home():
    return {"status": "API activa"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/info")
def info():
    return {
        "model_name": "Diabetes Predictor",
        "model_type": "RandomForestRegressor",
        "version": "1.0",
        "features": FEATURES
    }


@app.post("/predict")
def predict(data: PredictionRequest):

    global prediction_count
    global drift_count #nuevo

    prediction_count += 1
    REQUEST_COUNT.inc() #nuevo
    values = [[
        data.age,
        data.sex,
        data.bmi,
        data.bp,
        data.s1,
        data.s2,
        data.s3,
        data.s4,
        data.s5,
        data.s6
    ]]

    distance = np.mean( #inicio nuevo
        np.abs(np.array(values[0]) - baseline)
    )

    if distance > 0.2:

        drift_count += 1
        DRIFT_COUNT.inc() #nuevo

        logging.warning(
            f"DATA DRIFT DETECTED: {distance}"
        ) #fin nuevo

    prediction = model.predict(values) 

    logging.info(
        f"Input={data.dict()} Prediction={prediction[0]}"
    )

    return {
        "prediction": float(prediction[0])
    }
#nuevo inicio
# @app.get("/metrics")
# def metrics():
#     return {
#         "predictions": prediction_count,
#         "drift_alerts": drift_count
#     }

# @app.get("/monitor")
# def monitor():
#     drift_percentage = (
#         drift_count / prediction_count * 100
#         if prediction_count > 0 else 0
#     )
#     return {
#         "model": "Diabetes Predictor",
#         "version": "1.0",
#         "predictions": prediction_count,
#         "drift_alerts": drift_count,
#         "drift_percentage": drift_percentage,
#         "status": "healthy"
#     } #nuevo fin

# @app.get("/prometheus")
# def prometheus_metrics():

#     return Response(
#         generate_latest(),
#         media_type="text/plain"
#     )