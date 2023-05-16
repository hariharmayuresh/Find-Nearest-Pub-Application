import streamlit as st
import pandas as pd
import numpy as np
import os


#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest, "modified_open_pubs.csv")
df = pd.read_csv(DATA_PATH1)



# make header
st.header("Location of all Bars in UK")
# enter either postal code or local authority

local_author = st.selectbox('Select Local Authority : ', set(df['local_authority']))
button_1 = st.button("Submit")

if button_1:
    df_new = df.loc[(df['local_authority'] == local_author)]
    st.text("Total Number of Pubs in the location you entered are:")

    st.map(df_new)
    st.dataframe(df_new)
