import streamlit as st

# Custom CSS for card-like buttons
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

st.title("🏥 Health Care App")
st.write("Welcome to your personal health monitoring system. Select a module below to begin.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🩸\n\nBlood Report Analysis", use_container_width=True):
        st.switch_page("blood_report.py")

with col2:
    if st.button("⚖️\n\nBMI & Weight Tracking", use_container_width=True):
        st.switch_page("BMI_report.py")

with col3:
    if st.button("🩺\n\nHealth Care Assistant", use_container_width=True):
        st.switch_page("chatbot.py")
