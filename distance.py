from load_csv import load_distance_data, load_address_data

address_data = load_address_data()
distance_data = load_distance_data()


# Method for returning the index of an address. Called in following function to ensure proper data retrieval
def get_address_index(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])
    raise ValueError(f"Address {address} was not found in address_data")


# Method for getting the distance between two addresses using either their address string or index.
# Will be called in main.py in the package_delivery function
def get_distance(address_x, address_y):
    if isinstance(address_x, str):
        index_x = int(get_address_index(address_x))
    elif isinstance(address_x, int):
        index_x = int(address_x)
    else:
        raise ValueError(f"address_x should be an integer or string type, got {type(address_x)}")
    if isinstance(address_y, str):
        index_y = int(get_address_index(address_y))
    elif isinstance(address_y, int):
        index_y = int(address_y)
    else:
        raise ValueError(f"address_y should be an integer or string type, got {type(address_y)}")
    distance = distance_data[index_x][index_y]
    if distance == '':
        distance = distance_data[index_y][index_x]
    return float(distance)
