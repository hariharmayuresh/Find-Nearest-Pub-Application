

import streamlit as st
import numpy as numpy
import pandas as pd
from PIL import Image
from matplotlib import image
import os

st.title(':blue[Welcome to Find Nearest Pub Application ]')


#Adding image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "bartender.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)

st.subheader('Find the Basic information of the pub dataset')

DATA_PATH1 = os.path.join(dir_of_interest, "modified_open_pubs.csv")
df = pd.read_csv(DATA_PATH1)

choice = st.selectbox('',('Total pubs in UK','Head','Tail','unique local authority','null_values'))

if choice=='Total pubs in UK':
    st.markdown(f'There  are  **{df.shape[0]}**  Pubs  in  **United Kingdom**')

elif choice=='Head':
    st.dataframe(df.head())

elif choice=='Tail':
    st.dataframe(df.tail())

elif choice=='unique local authority':
    st.text(f'Total no of pub local authority is {len(df.local_authority.unique())} in UK')

elif choice=='null_values':
    st.markdown('**There are no null values in our dataset**')
    st.text(df.isnull().sum())

elif choice=='Statistics information':
     st.dataframe(df.describe())

st.text('')
st.text('')


#subheader
st.write('By: :blue[Mayuresh Harihar]')

btn_click = st.button("Connect with me")

if btn_click == True:
    st.write(":blue[LinkedIn]: (https://www.linkedin.com/in/mayuresh-harihar/)")

    st.write(":green[GitHub]: (https://github.com/hariharmayuresh)")

    st.write(":red[Instagram]: (https://www.instagram.com/hariharmayuresh/)")