import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="wide"
)

# -----------------------------
# Load model
# -----------------------------
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Title
# -----------------------------
st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details below.")
st.sidebar.header("Passenger Details")

st.sidebar.write(
    "Adjust the values and click the Predict button."
)

# -----------------------------
# User input
# -----------------------------
pclass = st.sidebar.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

sex = st.sidebar.selectbox(
    "Sex",
    ["Male", "Female"]
)

age = st.sidebar.slider(
    "Age",
    1,
    80,
    25
)

fare = st.sidebar.number_input(
    "Fare",
    min_value=0.0,
    value=20.0,
    step=1.0
)

sibsp = st.sidebar.number_input(
    "Siblings/Spouses",
    min_value=0,
    value=0,
    step=1
)

parch = st.sidebar.number_input(
    "Parents/Children",
    min_value=0,
    value=0,
    step=1
)

# -----------------------------
# Feature engineering
# -----------------------------
family_size = sibsp + parch + 1
is_alone = 1 if family_size == 1 else 0

sex = 1 if sex == "Male" else 0

embarked_c = 0
embarked_q = 0
embarked_s = 1

# -----------------------------
# Data frame
# -----------------------------
features = pd.DataFrame(
    [[
        pclass,
        sex,
        age,
        sibsp,
        parch,
        fare,
        embarked_c,
        embarked_q,
        embarked_s,
        family_size,
        is_alone,
    ]],
    columns=[
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked_C",
        "Embarked_Q",
        "Embarked_S",
        "FamilySize",
        "IsAlone",
    ],
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    prediction = model.predict(features)
    probability = model.predict_proba(features)

    survival_probability = probability[0][1] * 100

    st.subheader(
    f"Survival probability: {survival_probability:.2f}%"
)
    st.progress(int(survival_probability))
    if prediction[0] == 1:
        st.success("✅ Passenger survived.")
    else:
        st.error("❌ Passenger did not survive.")