from enum import Enum


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
        self.status = ShippingStatus.AT_HUB
        self.departure_time = None
        self.in_transit_time = None
        self.arrival_time = None

    # function for formatting the packages_on_truck object as strings
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s %s %s" % (
            self.package_id, self.package_address, self.city, self.state, self.zipcode,
            self.deadline, self.kilos, self.status.name, self.departure_time, self.in_transit_time,
            self.arrival_time,)

    # TODO
    # convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    def update_status(self, convert_timedelta):
        if self.arrival_time < convert_timedelta:
            self.status = ShippingStatus.DELIVERED
        elif self.departure_time > convert_timedelta:
            self.status = ShippingStatus.ON_TRUCK
        else:
            self.status = ShippingStatus.AT_HUB


# enumeration for packages_on_truck status
class ShippingStatus(Enum):
    DELIVERED = "DELIVERED"
    ON_TRUCK = "ON_TRUCK"
    AT_HUB = "AT_HUB"
