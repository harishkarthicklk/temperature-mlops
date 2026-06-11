import joblib

def test_model_loading():

    model = joblib.load("pkl_file/current_model.pkl")

    assert model is not None