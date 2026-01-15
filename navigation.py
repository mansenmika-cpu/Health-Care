import streamlit as st

navigation = st.Page("navigation.py", title="navigation Page")
home = st.Page("home.py", title="Home Page", icon=":material/home:")
BMI_report = st.Page("BMI_report.py", title="BMI Report", icon=":material/monitor_weight:")
blood_report = st.Page("blood_report.py", title="Blood Report", icon=":material/bloodtype:")
chatbot = st.Page("chatbot.py", title="Health Care Assistant", icon=":material/smart_toy:")

pg = st.navigation([home, blood_report, BMI_report, chatbot])

pg.run()
