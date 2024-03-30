# Name: Michael Lawrence
# Email: Mlaw101@wgu.edu
# Student ID: 002680987
import datetime

# from distance import get_distance
from hashtable import HashTable
from load_csv import load_distance_data, load_address_data, load_package_data
import truck

# load data into variables using functions from load_csv
address_data = load_address_data()
distance_data = load_distance_data()

package_hash_table = HashTable()
load_package_data("data/Packages.csv", package_hash_table)
# print(package_hash_table.lookup('1'))

# print(address_data)
#
# print(get_distance(2,6))
# print(get_distance("1330 2100 S (84106)", "2010 W 500 S (84104)"))
# print(get_distance("2010 W 400 S (84104)", "1330 2100 S (84106)"))


first_truck = truck.Truck(1, datetime.timedelta(hours=8))
first_truck.packages_on_truck = [13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 35, 37, 40]

second_truck = truck.Truck(2, datetime.timedelta(hours=10, minutes=20))
second_truck.packages_on_truck = [2, 3, 12, 17, 18, 21, 22, 23, 24, 28, 32, 36, 38, 39]

third_truck = truck.Truck(3, datetime.timedelta(hours=9, minutes=5))
third_truck.packages_on_truck = [1, 4, 5, 6, 7, 8, 9, 10, 11, 25, 26, 27, 28, 33, 35]
