# Name: Michael Lawrence
# Email: Mlaw101@wgu.edu
# Student ID: 002680987
import datetime

from hashtable import HashTable
from load_csv import load_distance_data, load_address_data, load_package_data
from truck import Truck, set_packages_in_progress

# load data into variables using functions from load_csv
address_data = load_address_data()
distance_data = load_distance_data()

package_hash_table = HashTable()
load_package_data("data/Packages.csv", package_hash_table)
print(package_hash_table.lookup('1'))


truck = Truck(1, datetime.timedelta(hours=8))
set_packages_in_progress(truck, package_hash_table)
#load_truck(truck, package_hash_table)
#
print(truck)
