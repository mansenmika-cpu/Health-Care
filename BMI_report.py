import streamlit as st

height = st.slider("Height (cm) : ", 0, 250, 170)
weight = st.slider("Weight (kg) : ", 0, 180, 60)

BMI = weight * 10000 / (height * height)

st.write("BMI Value : ", round(BMI, 2))

weight_category = ""

if BMI < 18.5:
    weight_category = "Underweight"

elif BMI < 25:
    weight_category = "Healthy Weight"

elif BMI < 29.9:
    weight_category = "Overweight"

else:
    weight_category = "Obese"

"Weight Category :", weight_category