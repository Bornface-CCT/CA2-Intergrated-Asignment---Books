# Importing libraries
import streamlit as st
import pandas as pd
import numpy as np

# Dashboard Title
st.title("Book Recommendation Dashboard")

DATE_COLUMN = 'date/time'
DATA = ('books.csv')

def load_data(nrows):
    data=pd.read_csv(books.csv)
    lowercase=lamba x:str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data
    
data_load_state=st.text('Loading Data...')
data=load_data(1000)
data_load_state.text('Loading Data Done!')

st.subheader("Dashboard Designed for Senior Citizens")
st.write(data)

# Large Font Styling
st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-size: 22px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Top Genres
st.header("Top categories")

Top_categories = books2['categories'].value_counts().head(10)

fig1 = px.bar(
    x=Top_categories.index,
    y=Top_categories.values,
    labels={'x':'categories', 'y':'Count'}
)

st.plotly_chart(fig1)

# Ratings Distribution
st.header("Ratings Distribution")

fig2 = px.histogram(
    books2,
    x='ratings_count',
    nbins=20
)

st.plotly_chart(fig2)

# Top Rated Books
st.header("Top Rated Books")

Top_Rated_Books = books2.groupby('title')['ratings_count'].mean().sort_values(ascending=False).head(10)

fig3 = px.bar(
    x=Top_Rated_Books.index,
    y=Top_Rated_Books.values
)

st.plotly_chart(fig3)

# Active Users
st.header("Most Books by Authors")

Most_Books_by_Authors = books2['authors'].value_counts().head(10)

fig4 = px.bar(
    x=Most_Books_by_Authors.index.astype(str),
    y=Most_Books_by_Authors.values
)

st.plotly_chart(fig4)