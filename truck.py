# Creating a Class for the trucks

class Truck:
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.capacity = 16
        self.speed = 18
        self.packages_on_truck = []
        self.mileage = 0
        self.truck_address = "4001 South 700 East"
        self.curr_time = start_time
        self.departure_time = start_time

    # Allows class to be read as a string
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.truck_id, self.capacity, self.speed, self.packages_on_truck,
                                               self.mileage, self.truck_address, self.departure_time)
