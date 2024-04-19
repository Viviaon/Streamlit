import streamlit as st
import pandas as pd
import plotly.express as px

# CSS code to make the width of columns match with lenght of text
st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
df_car["continent"] = df_car["continent"].apply(lambda x: x.replace(".", ""))
selected_df = df_car

st.title("Short analysis on cars attributes in different countries/continents")
st.divider()

c1 = st.container() #Not useful

st.header("Here is the data set")
selected_df

# Creation of buttons to allow the user to filter the country
st. write("You can filter on the continent / country")
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

boxAll = col1.button("All") # To unfilter

#Creation of the buttons (first attempts to create them with exec syntax -> didn't work)
# for ind, conti in enumerate(df_car["continent"].unique()):
#     exec(f"box{ind} = st.button({df_car['continent'].unique()[ind]})")
box1 = col2.button(df_car['continent'].unique()[0])
box2 = col3.button(df_car['continent'].unique()[1])
box3 = col4.button(df_car['continent'].unique()[2]) 

# Condition to filter the df based on the selection of the user
if box1 == True:
    selected_df = df_car[df_car["continent"] == df_car['continent'].unique()[0]]
elif box2 == True:
    selected_df = df_car[df_car["continent"] == df_car['continent'].unique()[1]]
elif box3 == True:
    selected_df = df_car[df_car["continent"] == df_car['continent'].unique()[2]]

# This loop was initially used for the button to filter the DF, it wasn't working
# I kept this to specify the selected filter
for ind, clicked in enumerate([box1, box2, box3]):
    if clicked == True:
        # selected_df = df_car[df_car["continent"] == df_car['continent'].unique()[ind]]
        click = df_car['continent'].unique()[ind]
    else:
        # selected_df = df_car
        click = "All"
               
st.caption(f"You've filtered on {click}")
                  
# First graph    
st.header("Correlation between Horsepower and MPG (Miles per Gallon)")

fig1 = px.scatter(selected_df, x = "hp", y = "mpg", 
                  color = "continent", 
                  labels = {"hp": "Horsepower",
                            "mpg": "Miles per Gallon",
                            "continent": "Continent"},
                  color_discrete_map = {"US": "red",
                                        "Europe" : "blue",
                                        "Japan": "green"})

fig1

st.write("You can see that there is a strong negative correlation between horsepower and MPG.")

# Second graph
st.header("Distribution of cylinder")

fig2 = px.histogram(selected_df, x = "cylinders", color = "continent",
                                      labels = {"cylinders": "Cylinders",
                                                "count": "Count",
                                                "continent": "Continent"},
                                      color_discrete_map = {"US": "red",
                                                            "Europe" : "blue",
                                                            "Japan": "green"})

fig2

st.write("Higher cylinders are exclusive to the US")
