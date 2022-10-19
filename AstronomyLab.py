#!/usr/bin/env python3
import requests
import datetime
ASTRONOMYAPI_ID="ffec605c-4849-47e2-9d8f-09e27e685875"
ASTRONOMYAPI_SECRET="134da5af70e33a2c5771fec6dc8e81cd2d52a34a5a1e880f40aa86d487a7c83a0ec8d2b9e2f12d7bb1078619b4bd32de963b6ed06da1e8e87c32438420a90658b6386be2086e706997438ce4ea03706e1e535163cd805dec3fab7c3f103c571190b733040db01aa78cdb9f0019702ac8"
def geo_location(): 
    response = requests.get("http://ip-api.com/json/44.208.120.75")
    events = response.json()
    return events 

test=geo_location()
long=test['lon']
lati=test['lat']
print(test['lat'], test['lon'])
def get_sun_position(latitude, longitude, body="sun"):
    """Returns the current position of the sun in the sky at the specified location
    Parameters:
    latitude (str)
    longitude (str)
    Returns:
    float: azimuth
    float: altitude
    """
    body = body
    url = f"https://api.astronomyapi.com/api/v2/bodies/positions/{body}"
    now = datetime.datetime.now()
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": 0,
        "from_date": now.date().isoformat(),
        "to_date": now.date().isoformat(),
        "time": now.strftime("%H:%M:%S"),
    }
    try:
        response = requests.get(
            url, params=params,
            auth=(ASTRONOMYAPI_ID, ASTRONOMYAPI_SECRET))
        if not response.status_code == 200:
            return None, None
    except requests.exceptions.ConnectionError:
        return None, None
    except requests.exceptions.Timeout:
        return None, None
    data = response.json()
    body_data = data["data"]["table"]["rows"][0]["cells"][0]
    position = body_data["position"]["horizontal"]
    alt = position["altitude"]["degrees"]
    az = position["azimuth"]["degrees"]
    return az, alt

def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates
    Parameters:
    azimuth (float)
    altitude (float)"""
    print(
        f"The Sun is currently at: "
        f"{altitude} deg altitude, {azimuth} deg azimuth."
    )

if __name__ == "__main__":
      t=get_sun_position(lati,long)
      azi=t[0]
      alt=t[1]
      p=print_position(azi,alt)
      print(p)