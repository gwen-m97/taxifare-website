import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
#Predict your taxifare
## Thank's to our AI model
''')


date = st.text_input('date and time (YYYY-MM-DD HH:MM)')
pick_long = st.text_input('pickup longitude')
pick_lat = st.text_input('pickup latitude')
drop_long =st.text_input('dropoff longitude')
drop_lat =st.text_input('dropoff latitude')
pass_count = st.text_input('passenger count')



url = 'https://taxifare.lewagon.ai/predict'



params = {
    "pickup_datetime": date,
    "pickup_longitude": pick_long,
    "pickup_latitude": pick_lat,
    "dropoff_longitude": drop_long,
    "dropoff_latitude": drop_lat,
    "passenger_count": pass_count
}

request = requests.get(url, params=params)
response_json = request.json()
prediction = response_json["fare"]

st.markdown(f'''Your taxi fare is : {prediction}
''')
