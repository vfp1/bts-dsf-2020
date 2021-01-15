import streamlit as st
from utils import HousePredict


if __name__ == "__main__":
    st.title('Housing price predictor')
    st.write('An app to know how much a house in California would cost')

    st.sidebar.header('Input variables from model for house prediction')

    st.sidebar.subheader('Input Longitude')
    st.sidebar.write('Beware that the model was built for California. A good default is -118')
    longitude = st.sidebar.slider('Select longitude', -180.0, 180.0, -118.0)

    st.sidebar.subheader('Input Latitude')
    st.sidebar.write('Beware that the model was built for California. A good default is 34')
    latitude = st.sidebar.slider('Select latitude', 0.0, 90.0, 34.0)

    st.sidebar.subheader('Input Housing Median Age')
    st.sidebar.write('Beware that the model was built for California. A good default is 18')
    housing_median_age = st.sidebar.slider('Select the median age of housing', 0, 100, 18)

    st.sidebar.subheader('Input Total Rooms in Neighbourhood')
    st.sidebar.write('Beware that the model was built for California. A good default is 3700')
    total_rooms = st.sidebar.slider('Select the rooms in the neighbourhood', 0.0, 10000.0, 3700.0)

    st.sidebar.subheader('Input Total Bedrooms in Neighbourhood')
    st.sidebar.write('Beware that the model was built for California. A good default is 400')
    total_bedrooms = st.sidebar.slider('Select the total bedrooms in neighbourhood', 0.0, 10000.0, 400.0)

    st.sidebar.subheader('Input Population')
    st.sidebar.write('Beware that the model was built for California. A good default is 3300')
    population = st.sidebar.slider('Select total population in neighbourhood', 0.0, 10000.0, 3300.0)

    st.sidebar.subheader('Input Total Households')
    st.sidebar.write('Beware that the model was built for California. A good default is 1400')
    households = st.sidebar.slider('Select total households per neighbourhood', 0.0, 10000.0, 1400.0)

    st.sidebar.subheader('Input Median Income')
    st.sidebar.write('Beware that the model was built for California. A good default is 2')
    median_income = st.sidebar.slider('Select the median income per month (in thousands)', 0.0, 100.0, 2.0)

    st.sidebar.subheader('Input Ocean Proximity')
    st.sidebar.write('You can only choose those options')
    ocean_distance = st.sidebar.selectbox('Select house ocean distance', options = ['<1H OCEAN', 'NEAR OCEAN', 'INLAND'])

    st.subheader('Selected values')
    pred, df = HousePredict().predict(longitude=longitude,
                                  latitude=latitude,
                                  housing_median_age=housing_median_age,
                                  total_rooms=total_rooms,
                                  total_bedrooms=total_bedrooms,
                                  population=population,
                                  households=households,
                                  median_income=median_income,
                                  ocean_proximity=ocean_distance)

    if st.checkbox("Show input DataFrame:"):
        st.write('The values that you have selected are')
        st.write(df.head())

    st.header('PREDICTED HOUSE PRICE!')
    st.write("Your selection of inputs result in a price of ", pred[0], " !!")

    st.map(df)





