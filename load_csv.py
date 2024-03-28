import csv

from hashtable import HashTable
from package import ShippingStatus, Package


# pull data from distance.py csv and adds to list
def load_distance_data():
    with open("data/Distance.csv") as distance_csv:
        distance_data = csv.reader(distance_csv)
        distance_data = list(distance_data)
    return distance_data


# pulls addresses from csv and adds to list
def load_address_data():
    with open("data/Address.csv") as address_csv:
        address_data = csv.reader(address_csv)
        address_data = list(address_data)
    return address_data


# function for populating hashtable with packages_on_truck objects created from the csv
def load_package_data(filename, package_hash_table):
    with open(filename, encoding='utf-8-sig') as package_CSV:
        package_data = csv.reader(package_CSV, delimiter=',')

        for package in package_data:
            package_id = package[0]
            package_address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight_kilos = package[6]
            status = ShippingStatus.AT_HUB

            # Creates packages_on_truck object
            p = Package(package_id, package_address, city, state, zipcode, deadline,
                        weight_kilos, status.name)

            # inserts packages_on_truck objects into hashtable
            package_hash_table.insert(package_id, p)
        # return ht
