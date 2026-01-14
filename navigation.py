import streamlit as st

navigation = st.Page("navigation.py", title="navigation Page")
home = st.Page("home.py", title="Home Page")
BMI_report = st.Page("BMI_report.py", title="BMI Report")
blood_report = st.Page("blood_report.py", title="Blood Report")

pg = st.navigation([home, blood_report, BMI_report])

pg.run()