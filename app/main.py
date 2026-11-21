from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("app/model.pkl")

FEATURES = [
    "age",
    "sex",
    "bmi",
    "bp",
    "s1",
    "s2",
    "s3",
    "s4",
    "s5",
    "s6"
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

    prediction = model.predict(values)

    return {
        "prediction": float(prediction[0])
    }