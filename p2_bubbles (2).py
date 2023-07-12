import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_excel(r"C:\Users\putri\Downloads\factbook(AutoRecovered).xlsx")

fig = px.scatter(df, x ="  GDP per capita ", y =" Life expectancy at birth",size ="  Population ", color =" Birth rate", hover_name ="Country", log_x = True, size_max = 60)

st.plotly_chart(fig, height = 1000, width = 1200)