import os
import pickle
import sys

sys.path.insert(1, "/Users/zainabshaikh/Disease Prediction/.venv/lib/python3.10/site-packages/streamlit_option_menu")

from streamlit_option_menu import option_menu
import streamlit as st 

st.set_page_config(page_title='Prediction of Disease Outbreak',
                   layout='wide',
                   page_icon='👩🏽‍⚕️'
                   )
diabetes_model = pickle.load(open(r"training_model/diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open(r"training_model/heart_model.sav",'rb'))
parkinson_model = pickle.load(open(r"training_model/parkinsons_model.sav",'rb'))
with st.sidebar:
    selected = option_menu("Prediction of disease outbreak system",['Diabetes Prediction','Heart Disease Prediction','Parkinson Prediction'],menu_icon="hospital-fill",icons = ['activity','heart','person'],default_index=0)
# Diabetes Predition
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose level")
    with col3 :
        Bloodpressure = st.text_input("Blood Preassure value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPredigreefunction = st.text_input("Diabetes Predigree Function value")
    with col2:
        Age = st.text_input("Age of the person")

    diab_diagnosis = ''
    if st.button("Diabetes Test Result"):
        user_input = [Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPredigreefunction,Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic "
    st.success(diab_diagnosis)

#Heart disease Prediction
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        person_age = st.text_input("age")
    with col2:
        sex = st.text_input("sex")
    with col3 :
        cp = st.text_input("cp")
    with col1:
        trestbps = st.text_input("trestbps")
    with col2:
        cholestrol = st.text_input("cholestrol")
    with col3:
        fbs = st.text_input("fbs")
    with col1:
        restecg = st.text_input("restecg")
    with col2:
        thalach = st.text_input("thalach")
    with col3:
        exang = st.text_input("exang")
    with col1:
        oldpeak = st.text_input("oldpeak")
    with col2:
        slope = st.text_input("slope")
    with col3:
        ca = st.text_input("ca")
    with col1:
        thal = st.text_input("thal")
    heart_disease_diagnosis=''
    if st.button("Heart Test Result"):
        user_input = [person_age,sex,cp,trestbps,cholestrol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        heart_disease_prediction = heart_disease_model.predict([user_input])
        if heart_disease_prediction[0]==1:
            heart_disease_diagnosis = "The person has a heart disease"
        else:
            heart_disease_diagnosis = "The person has a healthy heart "
    st.success(heart_disease_diagnosis)

#Parkinson Prediction
if selected == "Parkinson Prediction":
    st.title("Parkinson Prediction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3 :
        flo = st.text_input("MDVP:Flo(Hz)")
    with col1:
        jitter_per = st.text_input("MDVP:Jitter(%)")
    with col2:
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        rap = st.text_input("MDVP:RAP")
    with col1:
        ppq = st.text_input("MDVP:PPQ")
    with col2:
        ddp = st.text_input("Jitter:DDP")
    with col3:
        shimmer = st.text_input("MDVP:Shimmer")
    with col1:
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        apq3 = st.text_input("Shimmer:APQ3")
    with col3:
        apq5 = st.text_input("Shimmer:APQ5")
    with col1:
        apq = st.text_input("MDVP:APQ")
    with col2:
        dda = st.text_input("Shimmer:DDA")
    with col3:
        nhr = st.text_input("NHR")
    with col1:
        hnr = st.text_input("HNR")
    with col2:
        rpde = st.text_input("RPDE")
    with col3:
        dfa = st.text_input("DFA")
    with col1:
        spread1 = st.text_input("spread1")
    with col2:
        spread2 = st.text_input("spread2")
    with col3:
        d2 = st.text_input("D2")
    with col1:
        ppe = st.text_input("PPE")

    parkinson_diagnosis=''
    if st.button("Parkinson Test Result"):
        user_input = [fo,fhi,flo,jitter_per,jitter_abs,rap,ppq,ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]
        user_input = [float(x) for x in user_input]
        parkinson_prediction = parkinson_model.predict([user_input])
        if parkinson_prediction[0]==1:
            parkinson_diagnosis = "The person has a parkinson"
        else:
            parkinson_diagnosis = "The person doesn't have a parkinson"
    st.success(parkinson_diagnosis)  