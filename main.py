

import streamlit as st  # streamlit is library for creating web pages


def convert_units(value, unit_from, unit_to): # function to convert units
    conversions = {
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,   # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000,     # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    if key in conversions:
        return value * conversions[key]
    else:
        return None  # Return None if conversion is not supported

st.title("Unit Converter")

value = st.number_input("Enter a value to convert:", min_value=0.0, format="%.4f")
unit_from = st.selectbox("Select a unit to convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Select a unit to convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    if result is not None:
        st.success(f"Converted Value: {result:.4f} {unit_to}")
    else:
        st.error("Conversion not supported. Please select valid units.")


