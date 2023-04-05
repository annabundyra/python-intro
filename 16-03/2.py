import requests
from pprint import pprint as pp
from datetime import datetime

endpoint3 = "http://api.open-notify.org/iss-now.json"

response = requests.get(endpoint3)
print(response.status_code)

data = response.json()
print(data)

timestamp = data['timestamp']
dt_object = datetime.fromtimestamp(timestamp)
print("dt_object", dt_object)
print("type(dt_object) =", type(dt_object))

msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
    dt = dt_object,
    lat = data['iss_position']['latitude'],
    lon = data['iss_position']['longitude']
)
print(msg)

with open("space_station_location.txt", "a") as text_file:
    text_file.write(msg + '\n')
