import streamlit as st
import numpy as np
import pandas as pd
import joblib

gender = st.select_slider("Choose gender", ['Female', 'Male'])
SeniorCitizen = st.select_slider("Choose SeniorCitizen", [False, True])
Partner = st.select_slider("Choose Partner", [False, True])
Dependents = st.select_slider("Choose Dependents", [False, True])
tenure = st.number_input("Input tenure", 0,100)
PhoneService = st.select_slider("Choose PhoneService", [False, True])
MultipleLines = st.select_slider("Choose MultipleLines", ['No','No phone service', 'Yes'])
InternetService = st.select_slider("Choose InternetService", ['DSL','Fiber optic', 'NO'])
OnlineSecurity = st.select_slider("Choose OnlineSecurity", ['No','No internet service', 'Yes'])
OnlineBackup = st.select_slider("Choose OnlineBackup", ['No','No internet service', 'Yes'])
DeviceProtection = st.select_slider("Choose DeviceProtection", ['No','No internet service', 'Yes'])
TechSupport = st.select_slider("Choose TechSupport", ['No','No internet service', 'Yes'])
StreamingTV = st.select_slider("Choose StreamingTV", ['No','No internet service', 'Yes'])
StreamingMovies = st.select_slider("Choose StreamingMovies", ['No','No internet service', 'Yes'])
Contract = st.select_slider("Choose Contract", ['Month-to-month','Two year', 'One year'])
PaperlessBilling = st.select_slider("Choose PaperlessBilling", [False, True])
PaymentMethod = st.select_slider("Choose PaymentMethod", ['Electronic check','Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
MonthlyCharges = st.number_input("Input MonthlyCharges", 0,120)
TotalCharges = st.number_input("Input TotalCharges", 0,1000)
values = []
columns = ['gender','SeniorCitizen','Partner','Dependents', 'tenure', 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges']

if gender == 'Female' :
    sex = 0
elif gender == 'Male' :
    sex = 1
values = [sex,SeniorCitizen,Partner,Dependents, tenure, PhoneService, PaperlessBilling, MonthlyCharges, TotalCharges]
for i in ['No','No phone service', 'Yes']:
    columns.append('MultipleLines_'+i)
if MultipleLines == 'No' :
    values.append(1); values.append(0); values.append(0)
elif MultipleLines == 'No phone service' :
    values.append(0); values.append(1); values.append(0)
elif MultipleLines == 'Yes' :
    values.append(0); values.append(0); values.append(1)

for i in ['DSL','Fiber optic', 'NO']:
    columns.append('InternetService_'+i)
if InternetService == 'DSL' :
    values.append(1); values.append(0); values.append(0)
elif InternetService == 'Fiber optic' :
    values.append(0); values.append(1); values.append(0)
elif InternetService == 'NO' :
    values.append(0); values.append(0); values.append(1)

for i in ['No','No internet service', 'Yes']:
    columns.append('OnlineSecurity_'+i)
if OnlineSecurity == 'No' :
    values.append(1); values.append(0); values.append(0)
elif OnlineSecurity == 'No internet service' :
    values.append(0); values.append(1); values.append(0)
elif OnlineSecurity == 'Yes' :
    values.append(0); values.append(0); values.append(1)
        
for i in ['No','No internet service', 'Yes']:
    columns.append('OnlineBackup_'+i)
if OnlineBackup == 'No' :
    values.append(1); values.append(0); values.append(0)
elif OnlineBackup == 'No internet service' :
    values.append(0); values.append(1); values.append(0)
elif OnlineBackup == 'Yes' :
    values.append(0); values.append(0); values.append(1)

for i in ['No','No internet service', 'Yes']:
    columns.append('DeviceProtection_'+i)
if DeviceProtection == 'No' :
    values.append(1); values.append(0); values.append(0)
elif DeviceProtection == 'No internet service' :
    values.append(0); values.append(1); values.append(0)
elif DeviceProtection == 'Yes' :
    values.append(0); values.append(0); values.append(1)

for i in ['No','No internet service', 'Yes']:
    columns.append('TechSupport_'+i)
if TechSupport == 'No' :
    values.append(1); values.append(0); values.append(0)
elif TechSupport == 'No internet service' :
    values.append(0); values.append(1); values.append(0)
elif TechSupport == 'Yes' :
    values.append(0); values.append(0); values.append(1)
    
for i in ['No','No internet service', 'Yes']:
    columns.append('StreamingTV_'+i)
if StreamingTV == 'No' :
    values.append(1); values.append(0); values.append(0)
elif StreamingTV == 'No internet service' :
    values.append(0); values.append(1); values.append(0)
elif StreamingTV == 'Yes' :
    values.append(0); values.append(0); values.append(1)

for i in ['No','No internet service', 'Yes']:
    columns.append('StreamingMovies_'+i)
if StreamingMovies == 'No' :
    values.append(1); values.append(0); values.append(0)
elif StreamingMovies == 'No internet service' :
    values.append(0); values.append(1); values.append(0)
elif StreamingMovies == 'Yes' :
    values.append(0); values.append(0); values.append(1)

for i in ['Month-to-month','Two year', 'One year']:
    columns.append('Contract_'+i)
if Contract == 'Month-to-month' :
    values.append(1); values.append(0); values.append(0)
elif Contract == 'Two year' :
    values.append(0); values.append(1); values.append(0)
elif Contract == 'One year' :
    values.append(0); values.append(0); values.append(1)

for i in ['Electronic check','Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']:
    columns.append('Contract_'+i)
if PaymentMethod == 'Electronic check' :
    values.append(1); values.append(0); values.append(0); values.append(0)
elif PaymentMethod == 'Mailed check' :
    values.append(0); values.append(1); values.append(0); values.append(0)
elif PaymentMethod == 'Bank transfer (automatic)' :
    values.append(0); values.append(0); values.append(1); values.append(0)
elif PaymentMethod == 'Credit card (automatic)' :
    values.append(0); values.append(0); values.append(0); values.append(1)

model = joblib.load('C:/Users/Mojtaba/Desktop/python/streamlit/project2/Customer Churn.joblib')
def predict():
    row = np.array(values)
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)
    if prediction == 0 :
        st.error("Customer Not churn :material/thumb_down:")
    elif prediction == 1 :
        st.success("Customer churn :material/thumb_up:")
trigger = st.button('predict', on_click=predict)
