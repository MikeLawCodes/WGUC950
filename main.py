import csv

with open("data/Distance.csv") as distance_csv:
    distance_data = csv.reader(distance_csv)
    distance_data = list(distance_data)


def travel_distance(x_value, y_value):
    distance = distance_data[x_value][y_value]
    if distance == '':
        distance = distance_data[y_value][x_value]

    return float(distance)


with open("data/Address.csv") as address_csv:
    address_data = csv.reader(address_csv)
    address_data = list(address_data)


def extract_address(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])
