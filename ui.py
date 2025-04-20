import streamlit as st
import requests

# Judul aplikasi
st.title("Loan Application Prediction")

# Input form untuk berbagai fitur
loan_id = st.text_input("Loan ID (Unique ID for the loan)")
grade = st.selectbox("Grade", ["A", "B", "C", "D", "E", "F", "G"], index=0)
home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE"], index=0)
purpose = st.selectbox("Loan Purpose", [
    "debt_consolidation", "major_purchase", "car", "credit_card", "small_business", "other",
    "home_improvement", "medical", "vacation", "moving", "house", "renewable_energy", "wedding", "educational"
], index=0)
verification_status = st.selectbox("Verification Status", ["Source Verified", "Verified", "Not Verified"], index=0)
term = st.selectbox("Credit Term", ["36 months", "60 months"], index=0)
emp_length_int = st.number_input("Employment Length (years)", min_value=0, max_value=50, step=1, value=5)
mths_since_issue_d = st.number_input("Months Since Issue Date", min_value=0, step=1, value=40)
int_rate = st.number_input("Interest Rate", min_value=0.0, step=0.1, format="%.2f", value=5.0)
mths_since_earliest_cr_line = st.number_input("Months Since Earliest Credit Line", min_value=0, step=1, value=180)
acc_now_delinq = st.selectbox("Current Delinquencies", [0, 1, 2], index=0)
inq_last_6mths = st.selectbox("Inquiries in Last 6 Months", [0, 1, 2, 3, 4, 5, 6], index=0)
annual_inc = st.number_input("Annual Income", min_value=0, step=1000, value=50000)
dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, step=0.01, format="%.2f", value=10.0)

# Membuat dictionary untuk data input yang akan dikirim
input_data = {
    "loan_id": loan_id,
    "grade": grade,
    "home_ownership": home_ownership,
    "purpose": purpose,
    "verification_status": verification_status,
    "term": term,
    "emp_length_int": emp_length_int,
    "mths_since_issue_d": mths_since_issue_d,
    "int_rate": int_rate,
    "mths_since_earliest_cr_line": mths_since_earliest_cr_line,
    "acc_now_delinq": acc_now_delinq,
    "inq_last_6mths": inq_last_6mths,
    "annual_inc": annual_inc,
    "dti": dti
}


if st.button("Predict"):
    try:

        response = requests.post("https://cimb-data-science.onrender.com/predict", json=input_data)

        if response.status_code == 200:
            try:
                result = response.json()
                st.write("API Response (debug):", result)  # optional debug info

                if result is not None and 'prediction' in result and 'probability' in result:
                    prediction = "Default" if result['prediction'] == 0 else "No Default"
                    probability = result['probability']

                    st.success(f"Prediction: {prediction}")
                    st.write(f"Probability of Default: {probability:.2f}")
                else:
                    st.error("Prediction response is missing 'prediction' or 'probability' keys.")
            except Exception as e:
                st.error(f"Error decoding API response: {e}")
        else:
            st.error(f"Prediction failed. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
