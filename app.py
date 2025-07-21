import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Boston Housing Price Prediction")
st.write("Enter the values of the features below to predict the house price (in $1000s).")

# Sidebar inputs for features
st.sidebar.header("Input Features")

# These are some key features from the Boston dataset
CRIM = st.sidebar.number_input("Per capita crime rate (CRIM)", min_value=0.0, max_value=100.0, value=0.1)
ZN = st.sidebar.number_input("Proportion of residential land zoned (ZN)", min_value=0.0, max_value=100.0, value=18.0)
INDUS = st.sidebar.number_input("Proportion of non-retail business acres per town (INDUS)", min_value=0.0, max_value=30.0, value=10.0)
CHAS = st.sidebar.selectbox("Charles River dummy variable (CHAS) [0: no, 1: yes]", options=[0, 1])
NOX = st.sidebar.number_input("Nitric oxides concentration (NOX)", min_value=0.0, max_value=1.0, value=0.5)
RM = st.sidebar.number_input("Average number of rooms per dwelling (RM)", min_value=1.0, max_value=10.0, value=6.0)
AGE = st.sidebar.number_input("Proportion of owner-occupied units built prior to 1940 (AGE)", min_value=0.0, max_value=100.0, value=50.0)
DIS = st.sidebar.number_input("Weighted distances to employment centers (DIS)", min_value=0.0, max_value=15.0, value=5.0)
RAD = st.sidebar.number_input("Index of accessibility to highways (RAD)", min_value=1, max_value=24, value=4)
TAX = st.sidebar.number_input("Property tax rate (TAX)", min_value=100.0, max_value=1000.0, value=300.0)
PTRATIO = st.sidebar.number_input("Pupil-teacher ratio (PTRATIO)", min_value=10.0, max_value=30.0, value=18.0)
B = st.sidebar.number_input("Proportion of blacks by town (B)", min_value=0.0, max_value=400.0, value=350.0)
LSTAT = st.sidebar.number_input("% lower status population (LSTAT)", min_value=0.0, max_value=40.0, value=12.0)

# Create dataframe from inputs
input_data = pd.DataFrame({
    'CRIM': [CRIM],
    'ZN': [ZN],
    'INDUS': [INDUS],
    'CHAS': [CHAS],
    'NOX': [NOX],
    'RM': [RM],
    'AGE': [AGE],
    'DIS': [DIS],
    'RAD': [RAD],
    'TAX': [TAX],
    'PTRATIO': [PTRATIO],
    'B': [B],
    'LSTAT': [LSTAT]
})

# Predict button
if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction*1000:.2f}")

