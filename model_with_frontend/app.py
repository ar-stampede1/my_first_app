import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("forest_fire_model.pkl")  # Make sure this file is in the same directory as app.py

# Streamlit UI
st.title("🔥 Forest Fire Prediction App 🔥")
st.write("Enter environmental conditions to predict the likelihood of a forest fire.")

# Input fields for user
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)
RH = st.number_input("Relative Humidity (%)", min_value=0, max_value=100, step=1)
Ws = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=50.0, step=0.1)
Rain = st.number_input("Rainfall (mm)", min_value=0.0, max_value=50.0, step=0.1)
ffmc = st.number_input("Fine Fuel Moisture Code (FFMC)", min_value=0.0, max_value=100.0, step=0.1)
dmc = st.number_input("Duff Moisture Code (DMC)", min_value=0.0, max_value=200.0, step=0.1)
dc = st.number_input("Drought Code (DC)", min_value=0.0, max_value=1000.0, step=0.1)
isi = st.number_input("Initial Spread Index (ISI)", min_value=0.0, max_value=50.0, step=0.1)
bui = st.number_input("Buildup Index (BUI)", min_value=0.0, max_value=200.0, step=0.1)
fwi = st.number_input("Fire Weather Index (FWI)", min_value=0.0, max_value=50.0, step=0.1)

# Prediction Button
if st.button("Predict Fire Risk"):
    # Prepare input data
    input_data = pd.DataFrame([[temperature, RH, Ws, Rain, ffmc, dmc, dc, isi, bui, fwi]],
    columns=["Temperature", "RH", "Ws", "Rain", "FFMC", "DMC", "DC", "ISI", "BUI", "FWI"])


    # Make prediction
    prediction = model.predict(input_data)
    result = "🔥 Fire Risk Detected!" if prediction[0] == 1 else "✅ No Fire Risk."
    
    st.subheader(result)
