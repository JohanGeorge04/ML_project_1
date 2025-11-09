import pickle
from fastapi import FastAPI
import uvicorn
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer


app = FastAPI(title="diabetes-prediction")

with open('diabetes_model_xgb.bin', 'rb') as f_in:
    model,dv = pickle.load(f_in)


def predict_diabetes(patient_dict):
    X = dv.transform([patient_dict])
    dmatrix = xgb.DMatrix(X, feature_names=list(dv.get_feature_names_out()))

    prob = float(model.predict(dmatrix)[0])
    return prob


@app.post("/predict")
def predict(patient: dict):
    prob = predict_diabetes(patient)
    return {
        "diabetes_probability": prob,
        "diabetes_positive": prob >= 0.5
    }

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9090)




