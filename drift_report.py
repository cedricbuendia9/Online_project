import pandas as pd

from sklearn.datasets import load_diabetes

from evidently import Report
from evidently.presets import DataDriftPreset

# Dataset de referencia
data = load_diabetes()

columns = [
    "age", "sex", "bmi", "bp",
    "s1", "s2", "s3", "s4", "s5", "s6"
]

reference_data = pd.DataFrame(
    data.data,
    columns=columns
)

# Simulación de datos de producción
current_data = reference_data.copy()

# Forzamos drift en bmi
current_data["bmi"] = current_data["bmi"] * 3

report = Report(
    metrics=[DataDriftPreset()]
)

report.run(
    reference_data=reference_data,
    current_data=current_data
)

report.save("drift_report.html")

print("Reporte generado")