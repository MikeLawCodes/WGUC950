from load_csv import load_distance_data, load_address_data

address_data = load_address_data()
distance_data = load_distance_data()


# method for returning the index of an truck_address
def get_address_index(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])


# method for returning the truck_address from its index
def get_index_from_address(index):
    for row in address_data:
        if index == int(row[0]):
            return row[2]


# method for getting the distance between two addresses using either their string or index
def get_distance(address_x, address_y):
    index_x = get_address_index(address_x) if isinstance(address_x, str) else address_x
    index_y = get_address_index(address_y) if isinstance(address_y, str) else address_y

    distance = distance_data[index_x][index_y]
    if distance == '':
        distance = distance_data[index_y][index_x]

    return float(distance)
