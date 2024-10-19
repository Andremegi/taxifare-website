import streamlit as st
import datetime
import requests
import pandas as pd



'''
          # NY TAXI
            '''

col1, col2, col3, col4 = st.columns(4)

df_points= pd.DataFrame(
        [( 40.78, -73.95)],
        columns=["lat", "lon"])
with col1:

    date = st.date_input(
        "When ?",
        )

    time = st.time_input('At what time?',)
with col2:
    pick_up_latitude = st.number_input('Pick up latitude? ')
    pick_up_longitude = st.number_input('Pick up longitude? ')

with col3:
    drop_off_latitude = st.number_input('Drop_off latitude ?')
    drop_off_longitude = st.number_input('Drop_off longitude? ')

with col4:
    #passengers = st.number_input('Passengers')
    def get_select_box_data():

        return pd.DataFrame({
          'first column': list(range(1, 11)),

        })

    df = get_select_box_data()

    passengers = st.selectbox('Select a line to filter', df['first column'])



if st.button('Get fare'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    url= f'http://taxifare.lewagon.ai/predict?pickup_datetime={date}%20{time}&pickup_longitude={pick_up_longitude}&pickup_latitude={pick_up_latitude}&dropoff_longitude={drop_off_longitude}&dropoff_latitude={drop_off_latitude}&passenger_count={int(passengers)}'
    response = requests.get(url)

    response_json=response.json()

    st.write('Your fare is:', round(response_json['fare'],2), '$')
    st.metric("YOUR FARE ", f"${round(response_json['fare'],2)}")

    df_points= pd.DataFrame(
        [(pick_up_latitude, pick_up_longitude ),
        (drop_off_latitude, drop_off_longitude)],
        columns=["lat", "lon"]
    )

else:
    st.write('Click to have a fare amount 🚕 ')


st.map(df_points, color=(255,44,55), use_container_width=True, zoom =10)

CSS = """
h1 {
    text-align:center;
}

"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
