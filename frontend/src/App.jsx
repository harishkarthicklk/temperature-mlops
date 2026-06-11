import { useState } from "react";
import axios from "axios";



function App() {
  const [humidity, setHumidity] = useState("");
  const [pressure, setPressure] = useState("");
  const [windSpeed, setWindSpeed] = useState("");
  const [cloudCover, setCloudCover] = useState("");

  const [prediction, setPrediction] = useState("");

  const predictTemperature = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/predict",
        {
          humidity: Number(humidity),
          pressure: Number(pressure),
          wind_speed: Number(windSpeed),
          cloud_cover: Number(cloudCover),
        }
      );

      setPrediction(response.data.predicted_temperature);
    } catch (error) {
      console.error(error);
      alert("Prediction failed");
    }
  };

  return (
    
    <div style={{ padding: "30px" }}>
      <h1>Temperature Predictor</h1>

      <div>
        <label>Humidity</label>
        <br />
        <input
          type="number"
          value={humidity}
          onChange={(e) => setHumidity(e.target.value)}
        />
      </div>

      <br />

      <div>
        <label>Pressure</label>
        <br />
        <input
          type="number"
          value={pressure}
          onChange={(e) => setPressure(e.target.value)}
        />
      </div>

      <br />

      <div>
        <label>Wind Speed</label>
        <br />
        <input
          type="number"
          value={windSpeed}
          onChange={(e) => setWindSpeed(e.target.value)}
        />
      </div>

      <br />

      <div>
        <label>Cloud Cover</label>
        <br />
        <input
          type="number"
          value={cloudCover}
          onChange={(e) => setCloudCover(e.target.value)}
        />
      </div>

      <br />

      <button onClick={predictTemperature}>
        Predict Temperature
      </button>

      <br />
      <br />

      {prediction && (
        <h2>
          Predicted Temperature: {prediction.toFixed(2)} °C
        </h2>
      )}
    </div>
  );
}

export default App;