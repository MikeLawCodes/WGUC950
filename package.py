import csv


# Constructor class for package object

class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, kilos, notes):
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

    # function for formatting the package object as strings
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                          self.deadline, self.kilos, self.notes, self.departure_time,
                                                          self.arrival_time)


 # Function for populating hashtable with Package data and creating objects from that data
 def load_package_data(filename, ht):
    with open(filename, encoding='utf-8-sig') as package_CSV:
        package_data = csv.reader(package_CSV, delimiter=',')

        for package in package_data:
            pid = package[0]
            paddress = package[1]
            pcity = package[2]
            pstate = package[3]
            pzipcode = package[4]
            pdeadline = package[5]
            pkilos = package[6]
            pnotes = package[7]

            p = Package(pid, paddress, pcity, pstate, pzipcode, pdeadline,
                        pkilos, pnotes)

            ht.insert(pid, p)
