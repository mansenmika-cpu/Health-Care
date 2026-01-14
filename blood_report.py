import streamlit as st
import pandas as pd

age = st.slider("Age (years) : ", 0, 130, 50)

option = st.selectbox(
    "Gender : ",
    ("Male", "Female"),
    index=None,
    placeholder="Select gender...",
)

"CBC"

wbc = st.slider("WBC (mm\u00b3) : ", 0, 33000, 7000)
rbc = st.slider("RBC (million/mm\u00b3) : ", 0.0, 16.0, 4.5)
hgb = st.slider("HGB (g/dL) : ", 0.0, 50.0, 14.5)
hct = st.slider("HCT (%)", 0, 100, 42)
platelets = st.slider("Platelets (mm\u00b3) : ", 0, 900000, 300000)

"CMP"

glucose = st.slider("Glucose - Fasting (mg/dL) : ", 0, 300, 85)
sodium = st.slider("Sodium (mEq/dL) : ", 0, 300, 140)
pottasium = st.slider("Pottasium (mEq/dL) : ", 0.0, 15.0, 4.0)
creatinine = st.slider("Creatinine (mg/dL)", 0.0, 4.0, 0.9)
albumin = st.slider("Albumin (g/dL)", 0.0, 17.0, 4.2)
total_bilirubin = st.slider("Total Bilirubin (mg/dL)", 0.0, 4.0, 0.7)

lab_data = {
    "WBC (mm\u00b3)": wbc,
    "RBC (million/mm\u00b3)": rbc,
    "HGB (g/dL)": hgb,
    "HCT (%)": hct,
    "Platelets (mm\u00b3)": platelets,
    "Glucose - Fasting (mg/dL)": glucose,
    "Sodium (mEq/dL)": sodium,
    "Potassium (mEq/dL)": pottasium,
    "Creatinine (mg/dL)": creatinine,
    "Albumin (g/dL)": albumin,
    "Total Bilirubin (mg/dL)": total_bilirubin
}

def get_age_gender_effect(test, value, gender, age):
    is_male = gender == "Male"
    
    age_suffix = f" for a {age}-year-old {gender}."
    
    effects = {
        "WBC (mm³)": {
            "Low": "Reduced immune reserve; may be slower to fight infection.",
            "High": "Acute inflammatory response or infection signal.",
            "Normal": "Stable immune count" + age_suffix
        },
        "HGB (g/dL)": {
            "Low": "Anemia risk; might cause fatigue or shortness of breath.",
            "High": "Possible polycythemia; consider hydration or respiratory status.",
            "Normal": "Excellent oxygen carrying capacity" + age_suffix
        },
        "Creatinine (mg/dL)": {
            "Low": "Often seen with low muscle mass, common in aging or inactivity.",
            "High": "Kidney filtration is lower than expected for this age.",
            "Normal": f"Healthy kidney function; filtration rate is optimal for age {age}."
        },
        "Glucose - Fasting (mg/dL)": {
            "Low": "Low blood sugar; check caloric intake or medication.",
            "High": f"Elevated; metabolic risk increases significantly after age 45.",
            "Normal": "Strong metabolic control; glucose is well-managed."
        },
        "Albumin (g/dL)": {
            "Low": "Could indicate nutritional gaps or liver stress.",
            "High": "Typically indicates mild dehydration.",
            "Normal": "Good protein synthesis and liver health" + age_suffix
        }
    }

    default_map = {"Low": "Value is below range.", "High": "Value is above range.", "Normal": "Healthy value" + age_suffix}
    return effects.get(test, default_map)

def analyze_blood_report(data, gender, age):
    analysis_list = []

    ranges = {
        "WBC (mm³)": (4500, 11000),
        "RBC (million/mm³)": (4.5, 5.9) if gender == "Male" else (4.1, 5.1),
        "HGB (g/dL)": (14.0, 17.5) if gender == "Male" else (12.0, 15.5),
        "HCT (%)": (41.5, 50.4) if gender == "Male" else (36.9, 44.6),
        "Platelets (mm³)": (150000, 450000),
        "Glucose - Fasting (mg/dL)": (70, 99),
        "Sodium (mEq/dL)": (135, 145),
        "Potassium (mEq/dL)": (3.5, 5.2),
        "Creatinine (mg/dL)": (0.7, 1.3) if gender == "Male" else (0.6, 1.1),
        "Albumin (g/dL)": (3.4, 5.4),
        "Total Bilirubin (mg/dL)": (0.1, 1.2)
    }

    for test, value in data.items():
        low, high = ranges.get(test, (0, 0))
        
        if value < low:
            status = "Low"
            effect = get_age_gender_effect(test, value, gender, age)["Low"]
        elif value > high:
            status = "High"
            effect = get_age_gender_effect(test, value, gender, age)["High"]
        else:
            status = "Normal"
            effect = get_age_gender_effect(test, value, gender, age)["Normal"]
        
        analysis_list.append({
            "Test": test,
            "Result": value,
            "Reference Range": f"{low} - {high}",
            "Status": status,
            "Age & Gender Adjusted Effect": effect
        })
    
    return pd.DataFrame(analysis_list)

if option and age:
    df_report = analyze_blood_report(lab_data, option, age)
    df_report
else:
    st.warning("Select Gender.")    