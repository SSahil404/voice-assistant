import requests


def getInfo(city_name):
    api_key = "c3b47e9dbcdd4921b6d54727212903"
    base_url = "http://api.weatherapi.com/v1"
    URL = f"{base_url}/current.json?key={api_key}&q={city_name}&aqi=no"
    response = requests.get(URL).json()
    if 'error' in response:
        return response['error']['message']
    else:
        return f"Current Temperature in {city_name} is {response['current']['temp_c']} degree celcius."
