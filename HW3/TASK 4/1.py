

import requests
from pprint import pprint as pp

for i in range(1,7):

    endpoint = "https://pokeapi.co/api/v2/pokemon/{}/".format(i)

    response = requests.get(url = endpoint)
    print("response code: ", response.status_code)

    data = response.json()
    # pp(data)
    with open("pokemon.txt", "a") as file:
        file.writelines("Pokemon {} name: {}\n".format(i, data['name']))
        file.writelines("Pokemon {} height: {}\n".format(i, data['height']))
        file.writelines("Pokemon {} weight: {}\n".format(i, data['weight']))