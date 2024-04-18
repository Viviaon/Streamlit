import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Hello Wilders, welcome to my application!')

st.header("I enjoy to discover streamlit possibilities")

name = st.text_input("Please give me your name!")
name_lenght = len(name)
st.write(f"Your name has {name_lenght} characters")

st.divider()


st.subheader("Here is a first chart")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])
st.divider()

st.subheader("Here is a second chart made with Seaborn")
viz_correlation = sns.heatmap(df_weather.corr(numeric_only = True), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)