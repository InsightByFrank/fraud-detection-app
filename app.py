import streamlit as st
import pandas as pd
import pickle
import os

# -----------------------
# Page setup
# -----------------------

st.set_page_config(
    page_title="Fraud Detection App",
    layout="wide"
)

st.title("💳 Online Payment Fraud Detection")

# -----------------------
# Load model safely
# -----------------------

try:
    with open("fraud_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("model_columns.pkl", "rb") as f:
        model_columns = pickle.load(f)

except FileNotFoundError:
    st.error("Model files not found. Make sure fraud_model.pkl and model_columns.pkl are in this folder.")
    st.stop()

# -----------------------
# Layout
# -----------------------

col1, col2, col3 = st.columns(3)

# -----------------------
# Column 1
# -----------------------

with col1:
    st.subheader("Transaction Info")

    transaction_type = st.selectbox(
        "Transaction Type",
        ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"]
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0
    )

# -----------------------
# Column 2
# -----------------------

with col2:
    st.subheader("Sender Details")

    oldbalanceOrg = st.number_input(
        "Old Balance (Sender)",
        min_value=0.0
    )

    newbalanceOrig = st.number_input(
        "New Balance (Sender)",
        min_value=0.0
    )

# -----------------------
# Column 3
# -----------------------

with col3:
    st.subheader("Receiver Details")

    oldbalanceDest = st.number_input(
        "Old Balance (Receiver)",
        min_value=0.0
    )

    newbalanceDest = st.number_input(
        "New Balance (Receiver)",
        min_value=0.0
    )

# -----------------------
# Encoding (MATCH TRAINING)
# -----------------------

type_mapping = {
    "PAYMENT": 0,
    "TRANSFER": 1,
    "CASH_OUT": 2,
    "DEBIT": 3
}

type_encoded = type_mapping[transaction_type]

# -----------------------
# Feature Engineering
# -----------------------

balanceDiffOrig = oldbalanceOrg - newbalanceOrig
balanceDiffDest = newbalanceDest - oldbalanceDest

# -----------------------
# Create input dataframe
# -----------------------

input_data = pd.DataFrame({

    "type": [type_encoded],
    "amount": [amount],
    "oldbalanceOrg": [oldbalanceOrg],
    "newbalanceOrig": [newbalanceOrig],
    "oldbalanceDest": [oldbalanceDest],
    "newbalanceDest": [newbalanceDest],
    "balanceDiffOrig": [balanceDiffOrig],
    "balanceDiffDest": [balanceDiffDest]

})

# -----------------------
# Match training columns
# -----------------------

for col in model_columns:
    if col not in input_data:
        input_data[col] = 0

input_data = input_data[model_columns]

# -----------------------
# Prediction
# -----------------------

st.markdown("### Fraud Prediction")

center1, center2, center3 = st.columns([2,1,2])

with center2:

    if st.button("Check Transaction"):

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        st.metric(
            "Fraud Probability",
            f"{probability * 100:.1f}%"
        )

        if prediction == 1:
            st.error("⚠️ Fraudulent Transaction")
        else:
            st.success("✅ Legitimate Transaction")