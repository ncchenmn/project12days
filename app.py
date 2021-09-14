import streamlit as st
import pandas as pd
import numpy as np

st.title("Nina Chen's Milestone Project")



import requests



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
apikey = '53Y9LIQ9EUI6FSRI'
ticker = st.sidebar.text_input(label= 'Ticker (example: IBM)', value = "IBM")
month = st.sidebar.selectbox(label = 'Month', options = range(1,13))
year = st.sidebar.selectbox(label = 'Year', options = range(2010, 2022))
@st.cache
def load_data(ticker, month, year):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker +'&apikey=' + apikey + '&datatype=json&outputsize=full'
    r = requests.get(url)
    data = r.json()
    if 'Time Series (Daily)' in data:
        tmp = data['Time Series (Daily)']
        df = pd.DataFrame.from_dict(tmp, orient = 'index')
        df.index = pd.to_datetime(df.index,format='%Y-%m-%d')

        return df[(df.index.month== month)& (df.index.year == year)][['4. close']]



data_load_state = st.text('Loading data ....')
data = load_data(ticker, month, year)
data_load_state.text('Loading data ... done!')

st.subheader('Raw data')
st.write(data)