# Creating a Class for the trucks
from datetime import timedelta

import csv

import hashtable
from package import load_package_data


class Truck:
    max_capacity = 16
    avg_speed = 18

    def __init__(self, truck_id, capacity, speed, start_time):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.packages = []
        self.mileage = 0
        self.hub_address = "4001 South 700 East (84107)"
        self.time_object = start_time

    # Allows class to be read as a string
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.truck_id, self.capacity, self.speed, self.packages, self.mileage,
                                               self.hub_address, self.time_object)


