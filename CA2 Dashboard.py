# Importing libraries
import streamlit as st
import pandas as pd
import numpy as np

# Dashboard Title
st.title("Book Recommendation Dashboard")
st.subheader("Dashboard Designed for Senior Citizens")

DATE_COLUMN = 'date/time'
DATA = ('books.csv')

def load_data(nrows):
    data=pd.read_csv(books.csv)
    lowercase=lamba x:str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data
    
data_load_state=st.text('Loading Data...')
data+load_data(1000)
data_load_state.text('Loading Data Done!')