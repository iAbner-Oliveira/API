import requests
import json

# CONNECTION - API
# ______________________________________________________________________________________________________________________

# Set your API URL, for connection.
url = "https://YOUR_URL_FOR_CONNECTION"

# Define your parameters (Separate the parameters by "&").
payload = "Param1&Param2&param3&param4"

# If using header, set them here.
headers = {
    'Content-Type': "You Content-Type",
    'Cache-Control': "no-cache"
}
# Request data, pass parameters and data stored in variables.
response = requests.request("POST", url, data=payload, headers=headers)

# Output.
output = json.loads(response.text)

# Get data from an API parameter and store it in a variable - For connection.
data_get = output.get('access_token')

print(response.text)
print(data_get)

# DATA REQUEST
#  _____________________________________________________________________________________________________________________

# Set your API URL, for data request
url = "https://YOUR_URL_FOR_DATA_REQUEST"

# Define your parameters (Separate the parameters by "&")
payload = "Param1&Param2&param3&param4"

# If using header, set them here.
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Authorization': f"Bearer {data_get}"
}
# Request data, pass parameters and data stored in variable - For Data request.
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
