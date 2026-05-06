import streamlit as st
import pickle

# Load trained model
model = pickle.load(open('best_model.pkl', 'rb'))

# Title
st.title("📊 Walmart Sales Prediction App")

st.write("Enter the details below to predict weekly sales")

# Input fields
store = st.number_input("Store", min_value=1, value=1)
dept = st.number_input("Department", min_value=1, value=1)
temp = st.number_input("Temperature", value=25.0)
fuel = st.number_input("Fuel Price", value=3.0)
cpi = st.number_input("CPI", value=200.0)
unemp = st.number_input("Unemployment", value=8.0)

# Button
if st.button("Predict Sales"):
    try:
        prediction = model.predict([[store, dept, temp, fuel, cpi, unemp]])
        st.success(f"Predicted Weekly Sales: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")