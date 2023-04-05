import requests
from pprint import pprint as pp

pokemon_number = input("What is the pokemon number?: ")
endpoint = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon_number)

response = requests.get(url = endpoint)
print(response.status_code)

data = response.json()
pp(data)

pp(data['name'])
pp(data['height'])
pp(data['weight'])
pp(data['moves'])