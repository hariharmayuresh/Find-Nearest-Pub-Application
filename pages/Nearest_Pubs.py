import streamlit as st
import pandas as pd
import numpy as np
import os

#Page Header
st.header("Find Nearest Pubs")


#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest, "modified_open_pubs.csv")
df = pd.read_csv(DATA_PATH1)

#Take input latitude and longitude from user
lat=st.number_input(label="Enter Latitude Here", min_value=49.892485, max_value=60.764969)

lon=st.number_input(label="Enter Longitude Here", min_value=-7.384525, max_value=1.757763)


search_location=np.array((lat,lon))

original_location=np.array([df['latitude'],df['longitude']]).T

dist=np.sum((original_location-search_location)**2, axis=1)

df['Distance']=dist



df2=df.sort_values(by='Distance', ascending=True)[:5]

#List of Bar Names
st.subheader(f"Five nearest pubs for the Latitude and Longitube you entered:")

#Show Nearest Pubs on Map
st.map(data=df2, zoom=None, use_container_width=True)

#Name and Address of Nearby Pubs
st.table(df2[['name','address','local_authority']])