import streamlit as st
import google.generativeai as genai

# 1. API Configuration
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="BMI Report", page_icon="⚖️")
st.title("⚖️ BMI Calculator")

# 2. Input Parameters (Centered for better Mobile UX)
st.header("Input Parameters")
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("Height (cm) : ", 1, 250, 170)
with col2:
    weight = st.number_input("Weight (kg) : ", 1, 180, 60)

# 3. Calculation Logic
if height > 0:
    BMI = weight * 10000 / (height * height)
    bmi_val = round(BMI, 2)
else:
    bmi_val = 0

# 4. Category Logic
if bmi_val < 18.5:
    category, color = "Underweight", "#17a2b8"
elif bmi_val < 25:
    category, color = "Healthy Weight", "#28a745"
elif bmi_val < 29.9:
    category, color = "Overweight", "#ffc107"
else:
    category, color = "Obese", "#dc3545"

# 5. Display Result Card
st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 8px solid {color}; text-align: center;">
        <h3 style="color: #6c757d; margin-bottom: 0;">Your Calculated BMI</h3>
        <h1 style="font-size: 60px; color: {color}; margin-top: 0;">{bmi_val}</h1>
        <h2 style="color: {color};">{category}</h2>
    </div>
""", unsafe_allow_html=True)

st.info("BMI is a useful measure of overweight and obesity. It is calculated from your height and weight.")
st.divider()

# 6. AI Analysis Logic (Triggered by Button)
if st.button("🩺\n\nAnalyze Your BMI", use_container_width=True):
    # Important: Use an f-string to pass the actual bmi_val into the instructions
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
            
            # Save to session state so other pages can see the data
            st.session_state["user_bmi"] = bmi_val
            st.session_state["user_category"] = category
        except Exception as e:
            st.error(f"Error connecting to Gemini: {e}")
