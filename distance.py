
from load_csv import load_distance_data, load_address_data

address_data = load_address_data()
distance_data = load_distance_data()


# method for returning the index of an address
def get_address_index(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])


# method for getting the distance between two addresses using either their address string or index
def get_distance(address_x, address_y):
    if isinstance(address_x, str):
        index_x = int(get_address_index(address_x))
    else:
        index_x = int(address_x)
    if isinstance(address_y, str):
        index_y = int(get_address_index(address_y))
    else:
        index_y = int(address_y)

    distance = distance_data[index_x][index_y]
    if distance == '':
        distance = distance_data[index_y][index_x]
    return float(distance)


