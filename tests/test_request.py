import requests

payload = {
    "age": 0.038,
    "sex": 0.05,
    "bmi": 0.061,
    "bp": 0.021,
    "s1": -0.044,
    "s2": -0.034,
    "s3": -0.043,
    "s4": -0.003,
    "s5": 0.019,
    "s6": -0.017
}

response = requests.post(
    "http://localhost:5000/predict",
    json=payload
)

print(response.json())