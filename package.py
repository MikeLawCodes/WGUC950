import csv
from datetime import datetime, timedelta

from enum import Enum

import truck
from hashtable import HashTable


# Constructor class for packages_on_truck object
class Package:
    def __init__(self, package_id, package_address, city, state, zipcode, deadline, kilos, status):
        self.package_id = package_id
        self.package_address = package_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.kilos = kilos
        self.status = status
        self.departure_time = None
        self.in_transit_time = None
        self.arrival_time = None

    # function for formatting the packages_on_truck object as strings
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s %s %s" % (
            self.package_id, self.package_address, self.city, self.state, self.zipcode,
            self.deadline, self.kilos, self.status, self.departure_time, self.in_transit_time,
            self.arrival_time,)


# TODO
# convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


# enumeration for packages_on_truck status
class ShippingStatus(Enum):
    DELIVERED = "DELIVERED"
    ON_TRUCK = "ON_TRUCK"
    AT_HUB = "AT_HUB"
