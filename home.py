import streamlit as st

st.title("🏥 Health Care App")

st.header("", divider=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🩸 Open Blood Report", use_container_width=True):
        st.switch_page("blood_report.py")

with col2:
    if st.button("⚖️ Open BMI Report", use_container_width=True):
        st.switch_page("BMI_report.py")