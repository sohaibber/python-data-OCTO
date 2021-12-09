import streamlit as st
import pandas as pd
from src.constants import DATASET_PATH
from src.dashboard.eda import EDA
from src.dashboard.training import Training
from src.dashboard.inference import Inference
import time 

df = pd.read_csv(DATASET_PATH)
# Use the full page instead of a narrow central column
#st.set_page_config(layout="wide")

st.title("Card Fraud Detection Dashboard")
st.sidebar.title("Data Themes")

sidebar_options = st.sidebar.selectbox(
    "Options",
    ("EDA", "Training", "Inference")
)


if sidebar_options == "EDA":
    EDA(df)
    

elif sidebar_options == "Training":
    Training()

elif sidebar_options == "Inference":
    Inference()