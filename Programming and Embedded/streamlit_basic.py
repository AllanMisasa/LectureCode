import pandas as pd
import numpy as np
import sqlite3 as sql
import streamlit as st
import plotly_express as px

conn = sql.connect('C:/db/IoT.db') # Connect to the database

df = pd.read_sql_query('SELECT * FROM MEASUREMENTS', conn) # Read data from database into dataframe

print(df.head()) # Print first 5 rows of dataframe

formatted_dates = list(df['DATE']) # Format dates to be readable'
for i in formatted_dates:
    formatted_dates[formatted_dates.index(i)] = i[:22]

fig = px.histogram(df, x='DATE', y="TEMPERATURE", title = 'Temperature').update_xaxes(categoryorder = "total ascending") # Plot temperature data

fig.show()

'''
st.set_page_config(page_title='IoT Dashboard', layout='wide') # Set page title and layout

st.title('Smart City Dashboard') # Set page title

device_filter = st.selectbox('Filter by device', pd.unique(df['DEVICE_ID'])) # Create dropdown to filter by device

df = df[df['DEVICE_ID'] == device_filter] # Filter dataframe by device

m1, m2, m3 = st.columns(3) # Create 3 columns

m1.metric(
    label='Average temperature °C',
    value = df['TEMPERATURE'].mean(),
    ) # Create metric for temperature

m2.metric(
    value = df['HUMIDITY'].mean(),
    label='Average relative humidity in %',
    ) # Create metric for humidity

m3.metric(
    value = df['CO2'].mean(),
    label='C02s PPM',
    ) # Create metric for pressure

fig_col1, fig_col2 = st.columns(2) # Create 2 columns

with fig_col1:
    st.markdown('### Temperature chart') # Create header
    fig = px.area(df, x='DATE', y='TEMPERATURE') # Create line chart
    st.write(fig)

with fig_col2:
    st.markdown('### Humidity chart') # Create header
    fig2 = px.line(df, x='DATE', y='HUMIDITY') # Create line chart
    st.write(fig2)

st.markdown("### Detailed data view") # Create header
st.dataframe(df) # Create dataframe
'''