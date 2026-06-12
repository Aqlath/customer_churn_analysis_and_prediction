import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Load Model
model = joblib.load("churn_prediction.pkl")

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1 {
    color: #0f172a;
    text-align: center;
    font-weight: bold;
}

.stButton>button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 3em;
    border: none;
}

.stButton>button:hover {
    background-color: #1d4ed8;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Telecom Customer Churn Prediction")



st.markdown(
    """
    <h5 style='text-align: center;'>
    Predict whether a telecom customer is likely to churn based on
    customer demographics, services, billing, and contract details.
    </h5>
    """,
    unsafe_allow_html=True
)

st.divider()

# Layout Columns
col1, col2 = st.columns(2)

# LEFT COLUMN
with col1:

    st.subheader("👤 Customer Information")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

# RIGHT COLUMN
with col2:

    st.subheader("💳 Billing & Contract")

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

    total_charges = tenure * monthly_charges

    st.number_input(
        "Total Charges",
        value=float(total_charges),
        disabled=True
    )

st.divider()

# Predict Button
if st.button("Predict Customer Churn"):

    # Create Input DataFrame
    input_data = pd.DataFrame([[
        gender,
        partner,
        tenure,
        phone_service,
        internet_service,
        contract,
        paperless_billing,
        payment_method,
        monthly_charges,
        total_charges
    ]], columns=[
        'gender',
        'Partner',
        'tenure',
        'PhoneService',
        'InternetService',
        'Contract',
        'PaperlessBilling',
        'PaymentMethod',
        'MonthlyCharges',
        'TotalCharges'
    ])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    st.subheader("📈 Prediction Result")

    # Show Probability
    st.progress(float(probability))

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )

    # Prediction Output
    if prediction == 1:

        st.error(
            "⚠️ High Risk: Customer is likely to churn."
        )

        st.markdown("""
        ### Recommended Business Actions
        - Offer retention discounts
        - Provide long-term contract offers
        - Improve customer engagement
        - Offer loyalty benefits
        """)

    else:

        st.success(
            "✅ Low Risk: Customer is not likely to churn."
        )

        st.markdown("""
        ### Recommended Business Actions
        - Maintain customer satisfaction
        - Continue engagement programs
        - Promote premium services
        """)

st.divider()

st.caption("Built using Streamlit, Machine Learning, and Logistic Regression")
st.caption("by Mohammed Aqlath A")