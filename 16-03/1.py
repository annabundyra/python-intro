import requests
from pprint import pprint as pp

endpoint1 = "http://api.open-notify.org/astros.json"

response = requests.get(url = endpoint1)

print(response.status_code)

data = response.json()
pp(data['number'])
pp(type(data))

for person in data['people']:
    print(person['name'])

with open("astronauts.txt", "w") as text_file:
    for person in data['people']:
        text_file.write(person['name'] + '\n')
