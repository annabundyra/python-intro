
import requests
from pprint import pprint as pp

appid = 'f2a4d02c5689291bd4d7a105746d90f8'  # key to connect to the API --> create a free account and paste your OWN key here

endpoint = 'http://api.openweathermap.org/data/2.5/weather' # see doc to customise your payload

payload = {
    'q': 'London,UK',
    'unit': 'metrics',
    'appid': appid
}

response = requests.get(url=endpoint, params=payload)

data = response.json()


pp(data['name'])
pp(data['weather'])

pp(data)