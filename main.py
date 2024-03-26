import csv
import hashtable
from package import load_package_data

# pull data from distance csv and add to a list
with open("data/Distance.csv") as distance_csv:
    distance_data = csv.reader(distance_csv)
    distance_data = list(distance_data)


# method for finding distance between two points on the distance chart
def travel_distance(x_value, y_value):
    distance = distance_data[x_value][y_value]
    if distance == '':
        distance = distance_data[y_value][x_value]

    return float(distance)


# pull addresses from csv and add to list
with open("data/Address.csv") as address_csv:
    address_data = csv.reader(address_csv)
    address_data = list(address_data)


# method for returning the index of the address
def pull_address_index(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])


# method for returning the address from the index
def pull_index_from_address(index):
    for row in address_data:
        if index == int(row[0]):
            return row[2]


# function that finds the distance between two address strings using their indexes
def distance_between_addresses(address1, address2):
    x_value = pull_address_index(address1)
    y_value = pull_address_index(address2)
    return travel_distance(x_value, y_value)


# # test
# ht = hashtable.HashTable()
# load_package_data("data/Packages.csv", ht)
# print(ht)
# print(ht.search('18'))

# # test
# print(pull_address_index("177 W Price Ave (84115)"))
# print(pull_index_from_address(0))
