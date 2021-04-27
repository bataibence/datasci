import streamlit as st 
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import time

@st.cache
def load_data():
    data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')
    data['week'] = data.year_week.apply(lambda x: convert(x))
    return data

st.title("COVID-19 data")

country = st.sidebar.selectbox("Select a country", "{country}")
st.write(f"The selected country is {country}")

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 54
    return year + int(week)
    
data = load_data()

selected_country = data[data.country == {country}]

fig = px.line(data_frame = selected_country, x = 'week', y = 'cumulative_count', color = 'indicator', )

st.plotly_chart(fig)

