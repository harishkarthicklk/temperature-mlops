import joblib

model = joblib.load("pkl_file/current_model.pkl")

print("Model Type:", type(model).__name__)
print("Estimators:", getattr(model, "n_estimators", "N/A"))
print("Max Depth:", getattr(model, "max_depth", "N/A"))