import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("dataset/weather_v2.csv")

X = df.drop("temperature", axis=1)
y = df["temperature"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

with mlflow.start_run():

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)

    mlflow.log_param("n_estimators", 100)

    mlflow.log_metric("r2_score", r2)

    mlflow.sklearn.log_model(
        model,
        "temperature_model"
    )

    print("R²:", r2)