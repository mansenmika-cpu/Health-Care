import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="BMI Report", page_icon="⚖️")
st.title("⚖️ BMI Calculator")

st.header("Input Parameters")
col1, col2, col3, col4 = st.columns(4)
with col1:
    height = st.number_input("Height (cm) : ", 1, 250, 170)
with col2:
    weight = st.number_input("Weight (kg) : ", 1, 180, 60)
with col3:
    age = st.number_input("Age", 0, 150) 
with col4:
    gender = st.selectbox(
        "Gender : ",
        ("Male", "Female"),
        index=None,
        placeholder="Select gender...",
    )

if height > 0:
    BMI = weight * 10000 / (height * height)
    bmi_val = round(BMI, 2)
else:
    bmi_val = 0

if bmi_val < 18.5:
    category, color = "Underweight", "#17a2b8"
elif bmi_val < 25:
    category, color = "Healthy Weight", "#28a745"
elif bmi_val < 29.9:
    category, color = "Overweight", "#ffc107"
else:
    category, color = "Obese", "#dc3545"

st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 8px solid {color}; text-align: center;">
        <h3 style="color: #6c757d; margin-bottom: 0;">Your Calculated BMI</h3>
        <h1 style="font-size: 60px; color: {color}; margin-top: 0;">{bmi_val}</h1>
        <h2 style="color: {color};">{category}</h2>
    </div>
""", unsafe_allow_html=True)

st.write("")
st.info("BMI is a useful measure of overweight and obesity. It is calculated from your height and weight.")
st.divider()

st.markdown("""
    <style>
    div.stButton > button {
        height: 150px;    
        font-size: 20px;
        border-radius: 15px;
        border: 2px solid #0056b3;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #0056b3;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("🩺\n\nAnalyze Your BMI", use_container_width=True):
    system_instruction = f"""
    You are a specialized Health Care Assistant.
    The user has a BMI of {bmi_val}, which is categorized as {category}.
    1. Explain what this means for their health.
    2. Provide 3 actionable steps they should take.
    3. Mention potential risks (worst cases) if not managed.
    4. ALWAYS include a medical disclaimer.
    """

    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash',
        system_instruction=system_instruction
    )

    with st.spinner("AI Doctor is analyzing..."):
        try:
            response = model.generate_content(f"Provide a health analysis for a BMI of {bmi_val}")
            st.subheader("AI Health Analysis")
            st.markdown(response.text)
            
            st.session_state["user_bmi"] = bmi_val
            st.session_state["user_category"] = category
        except Exception as e:
            st.error(f"Error connecting to Gemini: {e}")



