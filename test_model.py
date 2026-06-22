import joblib
import pandas as pd

model = joblib.load("pkl_file/current_model.pkl")

df = pd.DataFrame([{
    "humidity":80,
    "pressure":1010,
    "wind_speed":10,
    "cloud_cover":50
}])

print(model.predict(df))
