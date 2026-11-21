import joblib

model = joblib.load("model.pkl")

print("Tipo:", type(model))
print("Entradas:", model.n_features_in_)