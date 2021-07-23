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


'''
{
    "location": {
        "name": "Guwahati",
        "region": "Assam",
        "country": "India",
        "lat": 26.18,
        "lon": 91.73,
        "tz_id": "Asia/Kolkata",
        "localtime_epoch": 1627006648,
        "localtime": "2021-07-23 7:47"
    },
    "current": {
        "last_updated_epoch": 1627002000,
        "last_updated": "2021-07-23 06:30",
        "temp_c": 29,
        "temp_f": 84.2,
        "is_day": 1,
        "condition": {
            "text": "Mist",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/143.png",
            "code": 1030
        },
        "wind_mph": 4.3,
        "wind_kph": 6.8,
        "wind_degree": 70,
        "wind_dir": "ENE",
        "pressure_mb": 999,
        "pressure_in": 30,
        "precip_mm": 4.6,
        "precip_in": 0.18,
        "humidity": 84,
        "cloud": 75,
        "feelslike_c": 38.2,
        "feelslike_f": 100.8,
        "vis_km": 4,
        "vis_miles": 2,
        "uv": 1,
        "gust_mph": 4.5,
        "gust_kph": 7.2
    }
}
'''
