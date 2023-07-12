import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel(r"D:\KULIAH\SEMESTER 4\VISDAT\TUGAS\Dataset_Visdat.xlsx")

#untuk memilih masing-masing atribut x,y, radius, color.
xVar = st.radio("Select variable X:", [" Area", " Birth rate", "  Current account balance ", " Death rate", " Electricity consumption", "  Electricity production", "  Exports", "  GDP ", "  GDP per capita", " GDP real growth rate", "  Highways", "  Imports", " Industrial production growth rate", " Infant mortality rate", " Inflation rate", "  Internet users", " Investment", "  Labor force", " Life expectancy at birth", " Military expenditures", "  Natural gas consumption", "  Oil consumption", "  Population", " Public debt", " Railways", "  Reserves of foreign exchange & gold", " Total fertility rate", " Unemployment rate"])
yVar = st.radio("Select variable Y:", [" Area", " Birth rate", "  Current account balance ", " Death rate", " Electricity consumption", "  Electricity production", "  Exports", "  GDP ", "  GDP per capita", " GDP real growth rate", "  Highways", "  Imports", " Industrial production growth rate", " Infant mortality rate", " Inflation rate", "  Internet users", " Investment", "  Labor force", " Life expectancy at birth", " Military expenditures", "  Natural gas consumption", "  Oil consumption", "  Population", " Public debt", " Railways", "  Reserves of foreign exchange & gold", " Total fertility rate", " Unemployment rate"])
sizeVar = st.radio("Select size variable:", [" Area", " Birth rate", "  Current account balance ", " Death rate", " Electricity consumption", "  Electricity production", "  Exports", "  GDP ", "  GDP per capita", " GDP real growth rate", "  Highways", "  Imports", " Industrial production growth rate", " Infant mortality rate", " Inflation rate", "  Internet users", " Investment", "  Labor force", " Life expectancy at birth", " Military expenditures", "  Natural gas consumption", "  Oil consumption", "  Population", " Public debt", " Railways", "  Reserves of foreign exchange & gold", " Total fertility rate", " Unemployment rate"])

clr = st.radio("Select color variable:", [" Area", "  Population ", "  Highways ", "  Internet users ", " Birth rate"])
hvr_name_col = "Country"

fig = px.scatter(df, x=xVar, y=yVar, size=sizeVar, color=clr, hover_name=hvr_name_col,
                 log_x=True, size_max=60)

fig.update_layout(
    title= "Bubble Chart")

# fig.update_traces(marker=dict(size=size_slider))
fig_brush = go.Figure(data=[go.Scatter(x=df["  GDP per capita "], y=df[" Life expectancy at birth"], mode="markers", opacity=0)])


fig_brush.data[0].on_hover(lambda trace, points, state: fig_brush.add_trace(go.Scatter(x=[p["x"] for p in points], y=[p["y"] for p in points], mode="markers", marker=dict(color="red", size=15))))
fig_brush.data[0].on_unhover(lambda trace, points, state: fig_brush.update_traces(selector=dict(mode="markers"), marker=dict(color="blue", size=5)))

fig.update_traces(x=df[xVar], y=df[yVar], marker_size=df[sizeVar])

st.plotly_chart(fig_brush)
st.plotly_chart(fig)

#dropdown list
select_col = st.selectbox("List Kolom", df.columns)

st.write(df[select_col])



