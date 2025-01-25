import streamlit as st
import numpy as np
import pandas as pd
import xgboost

# import ml package
import joblib
import os   

smoking = {'Yes': 1, 'No': 0}

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value
        
def load_scaler(scaler_file):
    loaded_scaler = joblib.load(open(os.path.join(scaler_file), 'rb'))
    return loaded_scaler
        
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def run_ml_app():
    st.markdown("<h2 style = 'text-align: center;'> Input Your Data </h2>", unsafe_allow_html=True)

    age = st.number_input("Age", 1, 100, value=25)
    mass = st.number_input('Mass (Kilograms)', 0, 200, value=70)
    height = st.number_input('Height (Meters)', 0.0, 2.5, value=1.7)
    excercise = st.number_input('Exercise frequency in a week', 0, 7, value=1)
    diet = st.slider("Diet quality", 0, 100, 75)
    sleep = st.number_input("Sleep hours in a day", 0, 24, value=7)
    smoke = st.radio('Smoking status', ['Yes','No'])
    alcohol = st.number_input("Alcohol consumption in a week", 0, 14, 2)

    bmi = mass/(height*height)
    
    result = {
            'Age': age,
            'BMI': bmi,
            'Exercise_Frequency': excercise,
            'Diet_Quality': diet,
            'Sleep_Hours': sleep,
            'Smoking_Status': smoke,
            'Alcohol_Consumption': alcohol
    }

    df = pd.DataFrame(
        {
            'Age': [age],
            'BMI': [bmi],
            'Exercise Frequency': [excercise],
            'Diet Quality': [diet],
            'Sleep Hours': [sleep],
            'Smoking Status': [smoke],
            'Alcohol Consumption': [alcohol]
        }
    )
    
    st.markdown("<h2 style = 'text-align: center;'>Your Data </h2>", unsafe_allow_html=True)

    st.dataframe(df)

    st.markdown("<h2 style = 'text-align: center;'> Prediction Result </h2>", unsafe_allow_html=True)

    encoded_result = []

    for i in result.values():
        if type(i) == int:
            encoded_result.append(i)
        elif type(i) == float:
            encoded_result.append(i)
        elif i in ['Yes', 'No']:
            res = get_value(i, smoking)
            encoded_result.append(res)

    single_array = np.array(encoded_result).reshape(1, -1)

    scaling = load_scaler("scaling.pkl")    
    scaling_array = scaling.transform(single_array)

    model = load_model("model_xgb.pkl")  
    prediction = model.predict(scaling_array)
    
    if prediction > 95:
        st.success("Healthy")
        st.write("Maintain your health and lifestyle.")
        st.markdown(
            """
            <ul>
                <li>Manage your BMI to stay ideal (18.5 - 25).</li>
                <li>Manage your diet.</li>
                <li>Manage your sleeping hours.</li>
                <li>Maintain exercise.</li>
                <li>Cut down on smoking.</li>
                <li>Cut down on alcohol.</li>
            </ul>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.warning("Not healthy enough")
        st.write("Improve your health and lifestyle.")
        st.markdown(
            """
            <ul>
                <li>Manage your BMI to stay ideal (18.5 - 25).</li>
                <li>Manage your diet.</li>
                <li>Manage your sleeping hours.</li>
                <li>Maintain exercise.</li>
                <li>Cut down on smoking.</li>
                <li>Cut down on alcohol.</li>
            </ul>
            """, 
            unsafe_allow_html=True
        )
