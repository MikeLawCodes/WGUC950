# Name: Michael Lawrence
# Email: Mlaw101@wgu.edu
# Student ID: 002680987
import csv
import datetime

import truck
from distance import get_distance, get_address_index
from hashtable import HashTable
from load_csv import load_distance_data, load_address_data, load_package_data
from package import ShippingStatus, Package


# load data
address_data = load_address_data()
distance_data = load_distance_data()

package_hash_table = HashTable()
load_package_data("data/Packages.csv", package_hash_table)
print(package_hash_table.lookup(4))

print(package_hash_table)
print(package_hash_table.lookup(39))


