from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_predict_endpoint():

    response = client.post(
        "/predict",
        json={
            "humidity": 70,
            "pressure": 1012,
            "wind_speed": 10,
            "cloud_cover": 40
        }
    )

    assert response.status_code == 200