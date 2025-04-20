from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from src import utils

app = FastAPI()

model = utils.deserialize_data("models/RandomForest.pkl")
if isinstance(model, tuple):  
    model = model[0]

ohe_home_ownership = utils.deserialize_data('models/ohe_home_ownership.pkl')
ohe_purpose = utils.deserialize_data('models/ohe_purpose.pkl')
ohe_verification_status = utils.deserialize_data('models/ohe_verification_status.pkl')
oe_grade = utils.deserialize_data('models/oe_grade.pkl')

class Item(BaseModel):
    loan_id: str
    grade: str
    home_ownership: str
    purpose: str
    verification_status: str
    term: str
    emp_length_int: int
    mths_since_issue_d: int
    int_rate: float
    mths_since_earliest_cr_line: int
    acc_now_delinq: int
    inq_last_6mths: int
    annual_inc: float
    dti: float

@app.post("/predict")
def predict(item: Item):
    try:
        # Preprocess term field
        term_numeric = 36 if item.term == "36 months" else 60
        data = pd.DataFrame([item.model_dump()])
        data['term'] = term_numeric  # Replace the term field with the numeric value

        home_ownership_encoded = ohe_home_ownership.transform(data[['home_ownership']])
        purpose_encoded = ohe_purpose.transform(data[['purpose']])
        verification_status_encoded = ohe_verification_status.transform(data[['verification_status']])
        grade_encoded = oe_grade.transform(data[['grade']])

        home_ownership_df = pd.DataFrame(home_ownership_encoded, columns=ohe_home_ownership.get_feature_names_out())
        purpose_df = pd.DataFrame(purpose_encoded, columns=ohe_purpose.get_feature_names_out())
        verfication_status_df = pd.DataFrame(verification_status_encoded, columns=ohe_verification_status.get_feature_names_out())
        grade_df = pd.DataFrame(grade_encoded, columns=oe_grade.get_feature_names_out())

        data = pd.concat([data, home_ownership_df, purpose_df, verfication_status_df, grade_df], axis=1)
        data.drop(columns=['home_ownership', 'purpose', 'verification_status','grade'], inplace=True)

        required_columns = list(model.feature_names_in_)
        for col in required_columns:
            if col not in data.columns:
                data[col] = 0

        data = data[required_columns]

        proba = model.predict_proba(data)[:, 1]
        if proba is None or len(proba) == 0:
            raise ValueError("Model returned empty probabilities.")

        threshold = 0.4615283093572654
        prediction = int(proba >= threshold)

        return {"prediction": prediction, "probability": proba[0]}

    except Exception as e:
        return {"error": str(e)}
