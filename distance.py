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
    global distance
    if isinstance(address_x, str):
        get_address_index(address_x)
        index_x = address_x
    else:
        index_x = int(address_x)
    if isinstance(address_y, str):
        get_address_index(address_y)
        index_y = address_y
    else:
        index_y = int(address_y)

        distance = distance_data[index_x][index_y]
    if distance == '':
        distance = distance_data[index_y][index_x]
    return float(distance)
