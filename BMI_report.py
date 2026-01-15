import streamlit as st

st.set_page_config(page_title="BMI Report", page_icon="⚖️")
st.title("⚖️ BMI Calculator")

# Sidebar for inputs to keep the main area clean
with st.sidebar:
    st.header("Input Parameters")
    height = st.slider("Height (cm) : ", 0, 250, 170)
    weight = st.slider("Weight (kg) : ", 0, 180, 60)

# Calculation
BMI = weight * 10000 / (height * height)
bmi_val = round(BMI, 2)

# Category Logic
if BMI < 18.5:
    category, color = "Underweight", "#17a2b8"
elif BMI < 25:
    category, color = "Healthy Weight", "#28a745"
elif BMI < 29.9:
    category, color = "Overweight", "#ffc107"
else:
    category, color = "Obese", "#dc3545"

# Display Result in a styled Card
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 8px solid {color}; text-align: center;">
        <h3 style="color: #6c757d; margin-bottom: 0;">Your Calculated BMI</h3>
        <h1 style="font-size: 60px; color: {color}; margin-top: 0;">{bmi_val}</h1>
        <h2 style="color: {color};">{category}</h2>
    </div>
""", unsafe_allow_html=True)

st.write("")

st.info("BMI is a useful measure of overweight and obesity. It is calculated from your height and weight.")
