import streamlit as st
import requests
import matplotlib.pyplot as plt
import time 
from src.constants import INFERENCE_EXAMPLE
from json import loads
import pandas as pd
import json 


def get_data():
    geted_result = requests.get(
                       'http://localhost:5000/api/inference',
                   ).text
    
    
    df = pd.read_json(geted_result, orient='index')
    st.table(df)

def Inference():
       st.header("Fraud Inference")
       st.info("This section simplifies the inference process. "
               "You can tweak the values of feature 1, 2, 19, "
               "and the transaction amount and observe how your model reacts to these changes.")
       feature_11 = st.slider('Transaction Feature 11', -10.0, 10.0, step=0.001, value=-4.075)
       feature_13 = st.slider('Transaction Feature 13', -10.0, 10.0, step=0.001, value=0.963)
       feature_15 = st.slider('Transaction Feature 15', -10.0, 10.0, step=0.001, value=2.630)
       amount = st.number_input('Transaction Amount', value=1000, min_value=0, max_value=int(1e10), step=100)
       infer = st.button('Run Fraud Inference')

       INFERENCE_EXAMPLE[11] = feature_11
       INFERENCE_EXAMPLE[13] = feature_13
       INFERENCE_EXAMPLE[15] = feature_15
       INFERENCE_EXAMPLE[28] = amount

       
       

       if infer:
           with st.spinner('Running inference...'):
               time.sleep(1)
               try:
                   result = requests.post(
                       'http://localhost:5000/api/inference',
                       json=INFERENCE_EXAMPLE
                   )
                   
                   if int(int(result.text) == 1):
                       st.success('Done!')
                       st.metric(label="Status", value="Transaction: Fraudulent")
                   else:
                       st.success('Done!')
                       st.metric(label="Status", value="Transaction: Clear")
                   get_data() 
               except Exception as e:
                   st.error('Failed to call Inference API!')
                   st.exception(e)