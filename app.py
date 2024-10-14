import streamlit as st
import requests



# Display a title and some information using Markdown
st.markdown('''
# Taxi Fare Prediction App
''')

# Section for user inputs
st.markdown('''
## Select Ride Parameters

Please provide the following details for your ride to retrieve a fare prediction:
''')

# Collecting user inputs using Streamlit widgets
pickup_date = st.date_input("Select pickup date")
pickup_time = st.time_input("Select pickup time")
pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, step=1)

# Combine date and time into a datetime string
pickup_datetime = f"{pickup_date} {pickup_time}"

# Button to submit
if st.button("Get Fare Prediction"):
    # API URL
    url = 'https://taxifare.lewagon.ai/predict'

    # Parameters to send to the API
    params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    # Call the API using the requests package
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        prediction = response.json().get('fare', 'No prediction available')
        st.success(f"Predicted Fare: ${prediction}")
    else:
        st.error("Failed to retrieve prediction. Please try again.")
