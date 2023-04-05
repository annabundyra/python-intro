from flights_data import flights

def search_flight(fid, flights):
    """Returns a list contain the flight with the specified id"""
    return [element for element in flights if element['flight_id'] == fid]


def get_index(fid, flights):
    """
    This function returns the index of the flight with the specified flight id
    :param fid: id of the flight
    :param flights: a list of dictionary flights
    :return: index of the flight in the flights list
    """
    for i, flight in enumerate(flights):
        if flight['flight_id'] == fid:
            return i
    return -1
