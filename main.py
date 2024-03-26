# Name: Michael Lawrence
# Email: Mlaw101@wgu.edu
# Student ID: 002680987

import csv
import hashtable
import truck
import datetime
from package import ShippingStatus, Package

# pull data from distance csv and add to a list
with open("data/Distance.csv") as distance_csv:
    distance_data = csv.reader(distance_csv)
    distance_data = list(distance_data)

# pull addresses from csv and add to list
with open("data/Address.csv") as address_csv:
    address_data = csv.reader(address_csv)
    address_data = list(address_data)


# method for returning the index of an address
def pull_address_index(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])


# method for returning the address from its index
def pull_index_from_address(index):
    for row in address_data:
        if index == int(row[0]):
            return row[2]


# method for finding distance between two addresses using their indexes as x and y values
def travel_distance(address_x, address_y):
    distance = distance_data[address_x][address_y]
    if distance == '':
        distance = distance_data[address_y][address_x]

    return float(distance)


first_truck = truck.Truck(1, 16, 18, datetime.timedelta(hours=8))
first_truck.packages = [13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 35, 37, 40]
#                       [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40],
second_truck = truck.Truck(2, 16, 18, datetime.timedelta(hours=10, minutes=20))
second_truck.packages = [2, 3, 12, 17, 18, 21, 22, 23, 24, 28, 32, 36, 38, 39]
#                       [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
third_truck = truck.Truck(3, 16, 18, datetime.timedelta(hours=9, minutes=5))
third_truck.packages = [1, 4, 5, 6, 7, 8, 9, 10, 11, 25, 26, 27, 28, 33, 35]
#                       [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]



