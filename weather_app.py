import requests
import streamlit as st
import pandas as pd

# URL for the weather API
url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

# Fetch the weather data
response = requests.get(url)
data = response.json()

# Extract temperature data
temperature_data = data['temperature']['data']

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(temperature_data)

# Add a sidebar for location selection
location = st.sidebar.selectbox("Select Location", df['place'])

# Filter the temperature data for the selected location
selected_location_data = df[df['place'] == location]

# Display the temperature of the selected location
st.title(f"Temperature at {location}")
st.write(f"Temperature: {selected_location_data['value'].values[0]} °C")

# Plot the temperature data as a bar chart
st.title("Current Temperature at Different Locations")
st.bar_chart(df.set_index('place')['value'])

# Alternatively, using matplotlib for more customization
fig, ax = plt.subplots()
ax.bar(df['place'], df['value'])
ax.set_xlabel('Place')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Current Temperature at Different Locations')
st.pyplot(fig)