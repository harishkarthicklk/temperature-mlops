import joblib
import pandas as pd

model = joblib.load("pkl_file/current_model.pkl")

sample = pd.DataFrame({
    "humidity": [70],
    "pressure": [1012],
    "wind_speed": [10],
    "cloud_cover": [40]
})

prediction = model.predict(sample)

print("Predicted Temperature:", prediction[0])