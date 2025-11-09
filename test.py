import requests

url = 'http://localhost:9696/predict'

patient = {'age': 42,
 'gender': 'Male',
 'ethnicity': 'Black',
 'education_level': 'Highschool',
 'income_level': 'Lower-Middle',
 'employment_status': 'Employed',
 'smoking_status': 'Current',
 'alcohol_consumption_per_week': 1,
 'physical_activity_minutes_per_week': 114,
 'diet_score': 6.7,
 'sleep_hours_per_day': 8.5,
 'screen_time_hours_per_day': 8.5,
 'family_history_diabetes': 0,
 'hypertension_history': 0,
 'cardiovascular_history': 1,
 'bmi': 24.7,
 'waist_to_hip_ratio': 0.84,
 'systolic_bp': 103,
 'diastolic_bp': 71,
 'heart_rate': 72,
 'cholesterol_total': 187,
 'hdl_cholesterol': 33,
 'ldl_cholesterol': 132,
 'triglycerides': 98,
 'glucose_fasting': 116,
 'glucose_postprandial': 172,
 'insulin_level': 5.7,
 'hba1c': 6.9
 }

response = requests.post(url, json=patient)
predictions = response.json()

print(predictions)

if predictions['diabetes_positive']:
    print("Patient likely has diabetes")
else:
    print("Patient unlikely to have diabetes")