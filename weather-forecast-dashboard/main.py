import streamlit as st
import plotly.express as px
from backend import get_data


st.title('Weather Forecast for the Next Days')


place = st.text_input('Place', placeholder='Type the city name here')
days = st.slider('Forecast Days', 1, 5)
selection = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f"{selection} for the next {days} days in {place}")


if place:
    try:
        filtered_data = get_data(place, days)

        if selection == "Temperature":
            temperatures = [entry["main"]["temp"] for entry in filtered_data]
            dates = [entry["dt_txt"] for entry in filtered_data]
            figure = px.line(x=dates, y=temperatures, title='Temperature Forecast', labels={'x': 'Date', 'y': 'Temperature (°C)'})
            st.plotly_chart(figure)

        elif selection == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [entry["weather"][0]["main"] for entry in filtered_data]
            image_paths = [images.get(condition, "images/cloud.png") for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("This place doesn't exist")