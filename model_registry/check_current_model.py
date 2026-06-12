import joblib
import os

MODEL_PATH = "pkl_file/current_model.pkl"

print("\n========== CURRENT MODEL ==========")

if os.path.exists(MODEL_PATH):

    model = joblib.load(MODEL_PATH)

    print(f"Model File : {MODEL_PATH}")
    print(f"Model Type : {type(model).__name__}")

    if hasattr(model, "n_estimators"):
        print(f"n_estimators : {model.n_estimators}")

    print("\nCurrent model loaded successfully")

else:

    print("Current model not found")