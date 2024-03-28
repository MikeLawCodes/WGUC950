# Creating a Class for the trucks
from datetime import timedelta

import csv

import hashtable
import package


class Truck:
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.capacity = 16
        self.speed = 18
        self.packages_on_truck = []
        self.mileage = 0
        self.truck_address = "4001 South 700 East (84107)"
        self.curr_time = start_time
        self.departure_time = start_time

    # Allows class to be read as a string
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.truck_id, self.capacity, self.speed, self.packages_on_truck,
                                               self.mileage, self.truck_address, self.departure_time)


def load_truck(self, ht):
    packages_on_truck = []
    pID = package.package_id
    if len(self.packages_on_truck) < self.capacity:
        self.packages_on_truck.append(ht.lookup(pID))
        return packages_on_truck
    else:
        return False


def set_packages_in_progress(self, package_hash_table):
    for package_id in self.packages_on_truck:
        packages_on_truck = package_hash_table.lookup(package_id)
        packages_on_truck.status = packages_on_truck.ShippingStatus.ON_TRUCK
        packages_on_truck.in_transit_time = self.departure_time
