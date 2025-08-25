import streamlit as st
import requests
import json

API_URL=  "http://127.0.0.1:8000/predict"

st.set_page_config("Insurance Premium Prediction", layout="centered")

st.title("Insurance Premium Prediction")

age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input(label="Weight", step=0.1)
height = st.number_input(label="Height", step=0.1)
income_lpa = st.number_input(label="Income in LPA", step=0.1)
smoker = st.checkbox(label="Smoker")
city = st.text_input(label = "City", placeholder="Enter City of user")
occupation = st.selectbox(label="Occupation",options=['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'])

if st.button("Predict"):
    
    payload= {
        "age":age,
        "weight": weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city":city,
        "occupation":occupation
    }
    payload = json.dumps(payload)

    response = requests.post(API_URL,payload)

    if response.status_code == 200:
        response = response.json()
        if "error" in response:
            st.error(response["error"])
        else:

           st.success(f"Prediction: {response['response']['predicted_category']}")
           st.success(f"Confidence: {response['response']['confidence']}")
