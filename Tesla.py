import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# STOCK PRICE: TESLA
""")

tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2000-01-01', end='2024-12-31')

st.write("## Closing Price")
st.line_chart(tickerDf.Close)

st.write("## Trading Volume")
st.line_chart(tickerDf.Volume)
