import json
from pprint import pprint

import requests

# GET Flights
result = requests.get('http://127.0.0.1:5000/flights')
pprint(result.json())

# GET a flight with specified id
# result = requests.get('http://127.0.0.1:5000/flights/555')
# pprint(result.json())

# POST REQUEST

new_flight = {
     "from_city": "Stockholm",
     "to_city": "Oslo",
     "days": [1, 7],
     "captain": {'name': 'Ole',
                 'surname': 'Johansson'},
     "duration_min": 30,
     "capacity": 50,
     "booked": 20,
     "available":  30,
     "flight_id": 777
}

headers = {'content-type': 'application/json'}
result = requests.post(
    url='http://127.0.0.1:5000/flights', headers=headers,    data=json.dumps(new_flight)
)
print(result.json())
print(result.status_code)
#

# # PUT REQUEST

updated_flight = {
     "new content": "test",
     "flight_id": 555
}

# fid = 555
#
# headers = {'content-type': 'application/json'}
# result = requests.put(
#     'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers, data=json.dumps(updated_flight)
# )
# pprint(result.json())
# # pprint(result.status_code)


# DELETE REQUEST

fid = 555

headers = {'content-type': 'application/json'}
result = requests.delete(
    'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers
)

print(result.status_code)
# print(result.json())
