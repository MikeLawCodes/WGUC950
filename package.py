from enum import Enum


class Package:
    def __init__(self, package_id, package_address, city, state, zipcode, deadline, kilos, truck_id, notes):  # Constructor function for Package object.
        self.package_id = package_id
        self.package_address = package_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.kilos = kilos
        self.truck_id = truck_id
        self.status = ShippingStatus.AT_HUB
        self.departure_time = None
        self.arrival_time = None
        self.notes = notes

    # Function for formatting the package object as strings.
    def __str__(self):
        return "%s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s" % (
            f'{self.package_id:11}', f'{self.package_address:39}', f'{self.city:16}', f'{self.state:6}',
            f'{self.zipcode:5}', f'{self.deadline:9}', f'{self.kilos:6}', f'{self.truck_id:9}', f'{self.status.name:10}',
            f'{str(self.departure_time):15}', f'{str(self.arrival_time):12}', f'{self.notes:59}')

    # Function to check the packages status based on converted time input.
    def update_status(self, converted_time_input):
        if self.arrival_time < converted_time_input:
            self.status = ShippingStatus.DELIVERED
        elif self.departure_time > converted_time_input:
            self.status = ShippingStatus.EN_ROUTE
        else:
            self.status = ShippingStatus.AT_HUB


# Enumeration for packages_on_truck status.
class ShippingStatus(Enum):
    DELIVERED = "DELIVERED"
    EN_ROUTE = "EN_ROUTE"
    AT_HUB = "AT_HUB"
