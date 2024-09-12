import json

# Sample JSON data (as a string for this example)
json_data = '''
{
    "endTime": "2024-09-11T19:45:00+08:00",
    "startTime": "2024-09-11T18:45:00+08:00",
    "rainfallFrom00To12": "",
    "rainfallJanuaryToLastMonth": "",
    "rainfallLastMonth": "",
    "tcmessage": "",
    "temperature": {
        "data": [
            {
                "place": "King's Park",
                "unit": "C",
                "value": 29
            },
            {
                "place": "Hong Kong Observatory",
                "unit": "C",
                "value": 30
            }
        ]
    }
}
'''

# Load the JSON data
data = json.loads(json_data)

# Extract temperature data
temperature_data = data.get('temperature', {}).get('data', [])

# Print the temperature of different locations
for entry in temperature_data:
    place = entry.get('place')
    value = entry.get('value')
    unit = entry.get('unit')
    print(f"Temperature at {place}: {value}°{unit}")