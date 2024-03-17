# Class for the packages to be delivered

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, kilos, notes):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilos = kilos
        self.notes = notes
        self.departure_time = None
        self.arrival_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                          self.deadline, self.kilos, self.notes, self.departure_time,
                                                          self.arrival_time)
