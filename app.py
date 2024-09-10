import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the models
diabetes_model = pickle.load(open('C:/Users/aksha/Ayushi/LifeGuard Diagnostics/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/aksha/Ayushi/LifeGuard Diagnostics/heart_disease_model.sav', 'rb'))
parkinson_model = pickle.load(open('C:/Users/aksha/Ayushi/LifeGuard Diagnostics/parkinson_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu("LifeGuard Diagnostics", 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title("Diabetes Predictor")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of pregnancies', min_value=0)
        SkinThickness = st.number_input('Skin Thickness Value', min_value=0.0)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0)
    with col2:
        Glucose = st.number_input('Glucose level', min_value=0.0)
        Insulin = st.number_input('Insulin Level', min_value=0.0)
        Age = st.number_input('Age', min_value=0)
    with col3:
        BloodPressure = st.number_input('Blood pressure', min_value=0.0)
        BMI = st.number_input('BMI', min_value=0.0)

    # Button for prediction
    if st.button('Get Result'):
        try:
            input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            diab_prediction = diabetes_model.predict(input_data)

            if diab_prediction[0] == 0:
                st.success('The person is not diabetic')
            else:
                st.success('The person is diabetic')
        except Exception as e:
            st.error(f"Error making prediction: {e}")

# Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Predictor')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=0)
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
        restecg = st.number_input('Resting Electrocardiographic results', min_value=0.0)
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0)
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', min_value=0)
    with col2:
        sex = st.selectbox('Sex', [0, 1])  # Assuming 0 and 1 are the valid options
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0.0)
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0.0)
        slope = st.number_input('Slope of the peak exercise ST segment', min_value=0)
    with col3:
        cp = st.number_input('Chest Pain types', min_value=0)
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0)
        exang = st.number_input('Exercise Induced Angina', min_value=0)
        ca = st.number_input('Major vessels colored by flourosopy', min_value=0)

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.success('The person is having heart disease')
            else:
                st.success('The person does not have any heart disease')
        except Exception as e:
            st.error(f"Error making prediction: {e}")

# Parkinson's Disease Prediction
elif selected == 'Parkinsons Disease Prediction':
    st.title("Parkinson's Disease Predictor")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
        RAP = st.number_input('MDVP:RAP', min_value=0.0)
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0)
        HNR = st.number_input('HNR', min_value=0.0)
        D2 = st.number_input('D2', min_value=0.0)
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0)
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0)
        RPDE = st.number_input('RPDE', min_value=0.0)
        PPE = st.number_input('PPE', min_value=0.0)
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)
        DDP = st.number_input('Jitter:DDP', min_value=0.0)
        APQ = st.number_input('MDVP:APQ', min_value=0.0)
        DFA = st.number_input('DFA', min_value=0.0)
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0)
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)
        DDA = st.number_input('Shimmer:DDA', min_value=0.0)
        spread1 = st.number_input('spread1', min_value=0.0)
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)
        NHR = st.number_input('NHR', min_value=0.0)
        spread2 = st.number_input('spread2', min_value=0.0)

    if st.button("Parkinson's Test Result"):
        try:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                          RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            parkinsons_prediction = parkinson_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's disease")
            else:
                st.success("The person does not have Parkinson's disease")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
