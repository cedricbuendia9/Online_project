# Diabetes Prediction API

API desarrollada con FastAPI que expone un modelo
RandomForestRegressor entrenado con el dataset Diabetes
de scikit-learn.

## Ejecutar

uvicorn main:app --reload

## Swagger

http://localhost:8000/docs

## Endpoint

POST /predict