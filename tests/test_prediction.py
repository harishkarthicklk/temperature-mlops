import joblib
import pandas as pd

def test_prediction():

    model = joblib.load("pkl_file/current_model.pkl")

    sample = pd.DataFrame({
        "humidity": [70],
        "pressure": [1012],
        "wind_speed": [10],
        "cloud_cover": [40]
    })

    prediction = model.predict(sample)

    assert prediction is not None
    assert len(prediction) == 1