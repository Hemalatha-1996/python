
# waather data forcase website


import streamlit as st
import plotly.express as px
from back_end import get_data

# Title of the web app
st.header("Weather Forecast for the Next Days")

# User input: place name
place=st.text_input("Place")

# User input: number of days to forecast
days=st.slider("Forecast days",min_value=1,max_value=5)

# User input: data type (Temperature or Sky)
option=st.selectbox("Select data to view",
                    ("Temperature","Sky"))
#plot name
st.subheader(f"{option} for the next {days} days in {place}")

if place:
   
    filtered_data=get_data(place,days)

    if option=="Temperature":
        date=[dict['dt_txt'] for dict in filtered_data]
        temperature=[dict["main"]["temp"] for dict in filtered_data]
        #plot 
        figure=px.line(x=date,y=temperature,labels={"X":"date","Y":"Temperature(c)"})
        st.plotly_chart(figure)
    
    if option=="Sky":
        images={"Clear":r"E:\Data analyst\python\udemy_python_course\projects\weather_forecast_dashboard\images\clear.png",
                "Clouds":r"E:\Data analyst\python\udemy_python_course\projects\weather_forecast_dashboard\images\cloud.png",
                "Rain":r"E:\Data analyst\python\udemy_python_course\projects\weather_forecast_dashboard\images\rain.png",
                "Snow":r"E:\Data analyst\python\udemy_python_course\projects\weather_forecast_dashboard\images\snow.png"}
        sky_condition=[dict["weather"][0]["main"] for dict in filtered_data]
        image_paths=[images[condition] for condition in sky_condition]
        st.image(image_paths,width=115)


        ## backend data


