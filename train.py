from pathlib import Path

import joblib
import numpy as np

from model import create_model
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
#nuevo 
#nuevo
import mlflow
import mlflow.sklearn

def train():

    data = load_diabetes()

    x = data.data
    y = data.target

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
    )

    # model = create_model()

    # model.fit(x_train, y_train)

    # predictions = model.predict(x_test)

    # mse = mean_squared_error(y_test, predictions)
    with mlflow.start_run():

        model = create_model()

        model.fit(x_train, y_train)

        predictions = model.predict(x_test)

        mse = mean_squared_error(
            y_test,
            predictions
        )

        mlflow.log_metric("mse", mse)

        mlflow.log_param(
            "model_type",
            "RandomForestRegressor"
        )

        # mlflow.sklearn.log_model(
        #     model,
        #     "model"
        # )
        mlflow.sklearn.log_model(
            sk_model=model,
            name="model",
            serialization_format="pickle"
        )

    print(f"MSE: {mse}")

    Path("app").mkdir(exist_ok=True)

    # Guardar modelo
    joblib.dump(model, "app/model.pkl")

    # Guardar baseline para monitoreo
    baseline = np.mean(x_train, axis=0)

    joblib.dump(
        baseline,
        "app/baseline.pkl"
    )

    print("Modelo guardado")
    print("Baseline guardado")


if __name__ == "__main__":
    train()