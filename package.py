import csv

from enum import Enum

import truck
from hashtable import HashTable


# Constructor class for package object
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, kilos, notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.kilos = kilos
        self.notes = notes
        self.departure_time = None
        self.arrival_time = None
        self.shipping_status = status

    # function for formatting the package object as strings
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s %s %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                             self.deadline, self.kilos, self.notes, self.departure_time,
                                                             self.arrival_time, self.shipping_status)

    # TODO
    def update_status(self, convert_time):
        if self.arrival_time < convert_time:
            self.shipping_status = ShippingStatus.DELIVERED
        elif self.departure_time > convert_time:
            self.shipping_status = ShippingStatus.IN_PROGRESS
        else:
            self.shipping_status = ShippingStatus.AT_HUB


# convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# Function for populating hashtable with Package data and creating objects from that data
def load_package_data(filename, ht):
    with open(filename, encoding='utf-8-sig') as package_CSV:
        package_data = csv.reader(package_CSV, delimiter=',')

        for package in package_data:
            package_id = package[0]
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight_kilos = package[6]
            if package[7] == '':
                special_notes = "Notes"
            else:
                special_notes = package[7]
            shipping_status = ShippingStatus.AT_HUB
            # Creates package object
            p = Package(package_id, address, city, state, zipcode, deadline,
                        weight_kilos, special_notes, shipping_status.name)

            # inserts package objects into hashtable
            ht.insert(package_id, p)


# enumeration for package shipping_status
class ShippingStatus(Enum):
    DELIVERED = "DELIVERED"
    IN_PROGRESS = "IN_PROGRESS"
    AT_HUB = "AT_HUB"

# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
