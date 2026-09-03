import streamlit as st
import pickle
import pandas as pd

model= pickle.load(open("model.pkl", "rb"))

st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("🩺 Diabetes Risk Score Predictor")

st.write(
    "Enter the patient's information below to predict "
    "the Diabetes Risk Score."
)


# =========================================================
# PATIENT INFORMATION
# =========================================================

st.header("👤 Patient Information")

col1, col2, col3 = st.columns(3)

with col1:
    Age = st.number_input(
        "Age",
        min_value=1.0,
        max_value=120.0,
        value=30.0
    )

with col2:
    Gender = st.selectbox(
        "Gender",
        ["Male", "Other", "Female"]
    )

with col3:
    Country = st.selectbox(
        "Country",
        [
            "Mexico",
            "Saudi Arabia",
            "Argentina",
            "United States",
            "Australia",
            "Bangladesh",
            "Germany",
            "Malaysia",
            "France",
            "Indonesia",
            "Turkey",
            "South Africa",
            "Nigeria",
            "Canada",
            "South Korea",
            "Spain",
            "Pakistan",
            "India",
            "Russia",
            "China",
            "Italy",
            "Egypt",
            "United Kingdom",
            "Brazil",
            "Japan"
        ]
    )


# =========================================================
# BODY MEASUREMENTS
# =========================================================

st.header("📏 Body Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    Height_cm = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=170.0
    )

with col2:
    Weight_kg = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=300.0,
        value=70.0
    )

with col3:
    BMI = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=24.0
    )

Waist_Circumference_cm = st.number_input(
    "Waist Circumference (cm)",
    min_value=30.0,
    max_value=200.0,
    value=85.0
)


# =========================================================
# BLOOD & MEDICAL MEASUREMENTS
# =========================================================

st.header("🩸 Blood & Medical Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    Blood_Glucose = st.number_input(
        "Blood Glucose",
        min_value=0.0,
        value=100.0
    )

with col2:
    HbA1c = st.number_input(
        "HbA1c",
        min_value=0.0,
        max_value=20.0,
        value=5.5
    )

with col3:
    Fasting_Blood_Sugar = st.number_input(
        "Fasting Blood Sugar",
        min_value=0.0,
        value=95.0
    )

col1, col2, col3 = st.columns(3)

with col1:
    Insulin_Level = st.number_input(
        "Insulin Level",
        min_value=0.0,
        value=10.0
    )

with col2:
    Blood_Pressure_Systolic = st.number_input(
        "Systolic Blood Pressure",
        min_value=50.0,
        max_value=250.0,
        value=120.0
    )

with col3:
    Blood_Pressure_Diastolic = st.number_input(
        "Diastolic Blood Pressure",
        min_value=30.0,
        max_value=150.0,
        value=80.0
    )


# =========================================================
# CHOLESTEROL & HEART
# =========================================================

st.header("❤️ Cholesterol & Heart Health")

col1, col2, col3 = st.columns(3)

with col1:
    Total_Cholesterol = st.number_input(
        "Total Cholesterol",
        min_value=0.0,
        value=180.0
    )

with col2:
    HDL = st.number_input(
        "HDL",
        min_value=0.0,
        value=50.0
    )

with col3:
    LDL = st.number_input(
        "LDL",
        min_value=0.0,
        value=100.0
    )

col1, col2 = st.columns(2)

with col1:
    Triglycerides = st.number_input(
        "Triglycerides",
        min_value=0.0,
        value=120.0
    )

with col2:
    Heart_Rate = st.number_input(
        "Heart Rate",
        min_value=30.0,
        max_value=220.0,
        value=72.0
    )


# =========================================================
# PHYSICAL ACTIVITY
# =========================================================

st.header("🏃 Physical Activity")

col1, col2, col3 = st.columns(3)

with col1:
    Physical_Activity_Level = st.selectbox(
        "Physical Activity Level",
        ["Moderate", "High", "Low"]
    )

with col2:
    Exercise_Hours_Per_Week = st.number_input(
        "Exercise Hours Per Week",
        min_value=0.0,
        max_value=100.0,
        value=3.0
    )

with col3:
    Daily_Walking_Minutes = st.number_input(
        "Daily Walking Minutes",
        min_value=0.0,
        max_value=1000.0,
        value=30.0
    )


# =========================================================
# DIET & LIFESTYLE
# =========================================================

st.header("🥗 Diet & Lifestyle")

col1, col2, col3 = st.columns(3)

with col1:
    Diet_Quality = st.selectbox(
        "Diet Quality",
        ["Healthy", "Average", "Poor"]
    )

with col2:
    Sugar_Intake_Level = st.selectbox(
        "Sugar Intake Level",
        ["Low", "High", "Moderate"]
    )

with col3:
    Sleep_Hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0
    )

col1, col2 = st.columns(2)

with col1:
    Stress_Level = st.selectbox(
        "Stress Level",
        ["Moderate", "High", "Low"]
    )

with col2:
    Smoking_Status = st.selectbox(
        "Smoking Status",
        ["Former", "Current", "Never"]
    )

Alcohol_Consumption = st.selectbox(
    "Alcohol Consumption",
    ["Never", "Frequently", "Occasionally"]
)


# =========================================================
# MEDICAL HISTORY
# =========================================================

st.header("🏥 Medical History")

col1, col2, col3 = st.columns(3)

with col1:
    Family_History_Diabetes = st.selectbox(
        "Family History of Diabetes",
        ["Yes", "No"]
    )

with col2:
    Hypertension = st.selectbox(
        "Hypertension",
        ["No", "Yes"]
    )

with col3:
    Heart_Disease = st.selectbox(
        "Heart Disease",
        ["Yes", "No"]
    )

col1, col2, col3 = st.columns(3)

with col1:
    Fatty_Liver = st.selectbox(
        "Fatty Liver",
        ["Yes", "No"]
    )

with col2:
    PCOS = st.selectbox(
        "PCOS",
        ["No", "Yes"]
    )

with col3:
    Medication_Adherence = st.selectbox(
        "Medication Adherence",
        ["Good", "Average", "Poor"]
    )


# =========================================================
# WORK & RESIDENCE
# =========================================================

st.header("🏠 Work & Residence")

col1, col2, col3 = st.columns(3)

with col1:
    Work_Type = st.selectbox(
        "Work Type",
        [
            "Retired",
            "Government",
            "Business",
            "Private",
            "Student"
        ]
    )

with col2:
    Residence_Type = st.selectbox(
        "Residence Type",
        ["Rural", "Urban"]
    )

with col3:
    Daily_Water_Intake_L = st.number_input(
        "Daily Water Intake (L)",
        min_value=0.0,
        max_value=20.0,
        value=2.0
    )


# =========================================================
# CREATE INPUT DATAFRAME
# =========================================================

input_data = pd.DataFrame([{

    "Age": Age,
    "Gender": Gender,
    "Country": Country,
    "Height_cm": Height_cm,
    "Weight_kg": Weight_kg,
    "BMI": BMI,
    "Waist_Circumference_cm": Waist_Circumference_cm,
    "Blood_Glucose": Blood_Glucose,
    "HbA1c": HbA1c,
    "Fasting_Blood_Sugar": Fasting_Blood_Sugar,
    "Insulin_Level": Insulin_Level,
    "Blood_Pressure_Systolic": Blood_Pressure_Systolic,
    "Blood_Pressure_Diastolic": Blood_Pressure_Diastolic,
    "Total_Cholesterol": Total_Cholesterol,
    "HDL": HDL,
    "LDL": LDL,
    "Triglycerides": Triglycerides,
    "Heart_Rate": Heart_Rate,
    "Physical_Activity_Level": Physical_Activity_Level,
    "Exercise_Hours_Per_Week": Exercise_Hours_Per_Week,
    "Daily_Walking_Minutes": Daily_Walking_Minutes,
    "Diet_Quality": Diet_Quality,
    "Sugar_Intake_Level": Sugar_Intake_Level,
    "Sleep_Hours": Sleep_Hours,
    "Stress_Level": Stress_Level,
    "Smoking_Status": Smoking_Status,
    "Alcohol_Consumption": Alcohol_Consumption,
    "Family_History_Diabetes": Family_History_Diabetes,
    "Hypertension": Hypertension,
    "Heart_Disease": Heart_Disease,
    "Fatty_Liver": Fatty_Liver,
    "PCOS": PCOS,
    "Medication_Adherence": Medication_Adherence,
    "Work_Type": Work_Type,
    "Residence_Type": Residence_Type,
    "Daily_Water_Intake_L": Daily_Water_Intake_L

}])


# =========================================================
# PREDICTION
# =========================================================

st.divider()

if st.button(
    "🔮 Predict Diabetes Risk Score",
    use_container_width=True
):

    try:

        prediction = model.predict(input_data)[0]

        st.success("Prediction completed successfully!")

        st.metric(
            label="🩺 Predicted Diabetes Risk Score",
            value=f"{prediction:.2f}"
        )

    except Exception as e:

        st.error("An error occurred while making the prediction.")

        st.exception(e)
