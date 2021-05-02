import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image
from plotly.subplots import make_subplots
import plotly.express as px 
import plotly.graph_objects as go
import time

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 54
    return year + int(week)


def load_data():
    data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')
    data['week'] = data.year_week.apply(lambda x: convert(x))
    return data
data = load_data()

st.title("COVID-19 data by country")

country_select = st.sidebar.selectbox("Select a country", data['country'].unique())
selected_country = data[data['country'] == country_select]
st.write(f"The selected country is", country_select)

fig = px.line(data_frame = selected_country, x = 'week', y = 'cumulative_count', color = 'indicator')

st.plotly_chart(fig)







