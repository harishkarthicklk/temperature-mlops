import joblib
import pandas as pd
import shutil
import sys
from sklearn.metrics import r2_score

# -------------------------
# CONFIGURATION
# -------------------------

TEST_DATASET = "dataset/weather_v3.csv"

CURRENT_MODEL = "pkl_file/current_model.pkl"

CANDIDATE_MODEL = "pkl_file/candidate/model_candidate.pkl"

# -------------------------
# LOAD DATASET
# -------------------------

df = pd.read_csv(TEST_DATASET)

X = df.drop("temperature", axis=1)
y = df["temperature"]

# -------------------------
# LOAD MODELS
# -------------------------

current_model = joblib.load(CURRENT_MODEL)

candidate_model = joblib.load(CANDIDATE_MODEL)

# -------------------------
# PREDICTIONS
# -------------------------

current_predictions = current_model.predict(X)

candidate_predictions = candidate_model.predict(X)

# -------------------------
# CALCULATE METRICS
# -------------------------

current_r2 = r2_score(y, current_predictions)

candidate_r2 = r2_score(y, candidate_predictions)

# -------------------------
# RESULTS
# -------------------------

print("\n==========================")
print("MODEL COMPARISON REPORT")
print("==========================")

print(f"Current Model R²  : {current_r2:.4f}")

print(f"Candidate Model R²: {candidate_r2:.4f}")

# -------------------------
# PROMOTION LOGIC
# -------------------------

if candidate_r2 > current_r2:

    print("\nCandidate model is BETTER")

    shutil.copy(
        CURRENT_MODEL,
        "pkl_file/backup/current_model_backup.pkl"
    )

    shutil.copy(
        CANDIDATE_MODEL,
        CURRENT_MODEL
    )

    print("Promotion Successful")

else:

    print("\nCandidate model is WORSE")

    print("Promotion Rejected")

    sys.exit(1)