import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

st.title("GDP Analysis Dashboard")

df = pd.read_csv('2020-2025.csv')
# clean data
df.fillna(0, inplace=True)

st.subheader("GDP Data overview")
st.dataframe(df)

# visualization of GDP data
df.rename(columns={
    'Country Name': 'Country',
    '2025 [YR2025]': '2025'
}, inplace=True)

# top highest GDP countries
st.subheader("Top 10 highest GDP countries")
highest_gdp = df.sort_values(by='2025', ascending=False).head(10)
st.dataframe(highest_gdp[['Country', '2025']])

# top lowest GDP countries
st.subheader("Top 10 lowest GDP countries")
lowest_gdp = df.sort_values(by='2025', ascending=True).head(10)
st.dataframe(lowest_gdp[['Country', '2025']])
