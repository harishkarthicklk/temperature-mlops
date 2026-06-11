import joblib

model = joblib.load("pkl_file/current_model.pkl")

print(type(model))
print(model)