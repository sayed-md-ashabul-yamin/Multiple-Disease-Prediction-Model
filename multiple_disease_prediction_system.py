

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("saved models/diabetes_model.sav", "rb"))

heart_disease_model = pickle.load(open("saved models/heart_disease_model(1).sav", "rb"))

parkinsons_model = pickle.load(open("saved models/parkinsons_model.sav", "rb"))


# sidebar for navigate

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System", 
                           
                         ["Diabetes Prediction", 
                          "Heart Disease Prediction", 
                          "Parkinson's Disease Prediction"],
                         
                         icons=["activity", "heart", "person"],
                         
                         default_index=0)
    
    
# diabetes page
if selected=="Diabetes Prediction":
    
    #page title
    st.title("Diabetes Prediction using ML")
    
    # getting the input data from the user
    # columns for input data
    col1, col2, col3 = st.columns(3, gap="medium")
    
    # input the data
    
    with col1:
      Pregnancies = st.text_input("Number of Pregnancies")
      
    with col2:
      Glucose = st.text_input("Glucose Level")
    
    with col3:
      BloodPressure = st.text_input("Blood Pressure Value")
    
    with col1:
      SkinThickness = st.text_input("Skin Thickness Value")
    
    with col2:
      Insulin = st.text_input("Insulin Level")
    
    with col3:
      BMI = st.text_input("BMI Value")
    
    with col1:
      DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    
    with col2:
      Age = st.text_input("Age of The Person")
    
    
    # Code for prediction
    diab_diagnosis = ""
    
    # Creating a button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if diab_prediction[0]==1:
           diab_diagnosis = "The Person is Diabetic"
          
        else:
           diab_diagnosis = "The Person is Non-Diabetic"
          
     
    st.success(diab_diagnosis)
        
        

# Heart Disease page
if selected=="Heart Disease Prediction":
    
    #page title
    st.title("Heart Disease Prediction using ML")
    
    
    # getting the input data from the user
    # columns for input data
    col1, col2, col3 = st.columns(3, gap="medium")
    
    # input the data
    
    with col1:
      age = st.text_input("Age of The Person")
      
    with col2:
      sex = st.text_input("sex of The Person")
    
    with col3:
      cp = st.text_input("Chest Pain Type")
    
    with col1:
      trestbps = st.text_input("Resting Blood Pressure")
    
    with col2:
      chol = st.text_input("Serum Cholestoral (mg/dl)")
    
    with col3:
      fbs = st.text_input("Fasting Blood Sugar")
    
    with col1:
      restecg = st.text_input("Resting Electrocardiographic Results")
    
    with col2:
      thalach = st.text_input("Maximum Heart Rate achieved")
      
    with col3:
      exang = st.text_input("Exercise induced Angina")
      
    with col1:
      oldpeak = st.text_input("Oldpeak = ST depression induced by exercise relative to rest")
      
    with col2:
      slope = st.text_input("Slope of the Peak Exercise ST Segment")
      
    with col3:
      ca = st.text_input("Number of Major Vessels (0-3) Colored by Flourosopy")
      
    with col1:
      thal = st.text_input("THAL: 0 = normal; 1 = fixed defect; 2 = reversable defect")
      
      
    
    
    # Code for prediction
    heart_diagnosis = ""
    
    # Creating a button for prediction
    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
        if heart_prediction[0]==1:
            heart_diagnosis = "The Person has Heart Disease"
          
        else:
            heart_diagnosis = "The Person has Healthy Heart"
          
     
    st.success(heart_diagnosis)
    

# Parkinson's Disease page
if selected=="Parkinson's Disease Prediction":
    
    #page title
    st.title("Parkinson's Disease Prediction using ML")
    
    # input the data
    col1, col2, col3 = st.columns(3, gap="large")  
    
    with col1:
        fo = st.text_input('MDVP : Fo(Hz) - Average Vocal Fundamental Frequency')
        
    with col2:
        fhi = st.text_input('MDVP : Fhi(Hz) - Maximum Vocal Fundamental Frequency')
        
    with col3:
        flo = st.text_input('MDVP : Flo(Hz) - Minimum Vocal Fundamental Frequency')
        
    with col1:
        Jitter_percent = st.text_input('MDVP : Jitter(%) - Variation in Fundamental Frequency')
        
    with col2:
        Jitter_Abs = st.text_input('MDVP : Jitter(Abs) - Variation in Fundamental Frequency')
        
    with col3:
        RAP = st.text_input('MDVP : RAP - Variation in Fundamental Frequency')
        
    with col1:
        PPQ = st.text_input('MDVP : PPQ - Variation in Fundamental Frequency')
        
    with col2:
        DDP = st.text_input('Jitter : DDP - Variation in Fundamental Frequency')
        
    with col3:
        Shimmer = st.text_input('MDVP : Shimmer - Variation in Amplitude')
        
    with col1:
        Shimmer_dB = st.text_input('MDVP : Shimmer(dB) - Variation in Amplitude')
        
    with col2:
        APQ3 = st.text_input('Shimmer : APQ3 - Variation in Amplitude')
        
    with col3:
        APQ5 = st.text_input('Shimmer : APQ5 - Variation in Amplitude')
        
    with col1:
        APQ = st.text_input('MDVP : APQ - Variation in Amplitude')
        
    with col2:
        DDA = st.text_input('Shimmer : DDA - Variation in Amplitude')
        
    with col3:
        NHR = st.text_input('NHR - Ratio of Noise to Tonal Components in the Voice')
        
    with col1:
        HNR = st.text_input('HNR - Ratio of Noise to Tonal Components in the Voice')
        
    with col2:
        RPDE = st.text_input('RPDE - Nonlinear Dynamical Complexity Measures')
        
    with col3:
        DFA = st.text_input('DFA - Signal Fractal Scaling Exponent')
        
    with col1:
        spread1 = st.text_input('spread1 - Nonlinear Measure of Fundamental Frequency Variation')
        
    with col2:
        spread2 = st.text_input('spread2 - Nonlinear Measure of Fundamental Frequency Variation')
        
    with col3:
        D2 = st.text_input('D2 - Nonlinear Dynamical Complexity Measures')
        
    with col1:
        PPE = st.text_input('PPE - Nonlinear Measures of Fundamental Frequency Variation')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
