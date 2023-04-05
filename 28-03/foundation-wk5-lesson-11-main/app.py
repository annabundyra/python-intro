from flask import Flask, jsonify, request

from flights_data import flights
from utils import search_flight, get_index

app = Flask(__name__)


# GETTING INFORMATION

@app.route('/')
def hello():
    return {'hello': 'Universe'}

# @app.route('/hello-cfg')
# def hello_cfg():
#     return {'hello': 'cfg'}

@app.route('/flights', methods = ['GET'])
def get_flights():
    return jsonify(flights)

#
# # htttp://127.0.0.01/flights/1
@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)

#
# # GET a resource / resources - GET method
# # ADD a resource - POST method
# # DELETE a resource - DELETE method
# # EDIT a resource - PUT method / PATCH method
#
#
# # ADDING A FLIGHT RESOURCE - POST METHOD

@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    flights.append(flight)
    return jsonify(flight)
#
#
# # UPDATE A FLIGHT

@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flights[index])


# @app.route('/flights/<int:id>', methods=['DELETE'])
# def delete_flght(id):
#     index = get_index(fid=id, flights=flights)
#     deleted = flights.pop(index)
#     return jsonify(deleted)
#

if __name__ == '__main__':
    app.run(debug=True)
