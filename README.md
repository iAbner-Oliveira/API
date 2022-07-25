<h1 align="left"> API - PYTHON </h1>

Script made in python to connect and request data


## :snake: Functionality for Script.

- `Functionality 1`: Python script for connecting and requesting data via API.
- `Functionality 2`: Creating graphics with the pandas library

## Setup

### Python Version

It is recommended that for full script functionality the Python version is `3.9` or higher.

### Install and add to the following Python libraries;

```xml
pip install requests
```

```xml
pip install json
```



### Add a Libraries on Python to your script.

To use the script, you need to have the following `<libraries>` installed;


## :snake: Script

```python
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
```
