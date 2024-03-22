import csv

from hashtable import HashTable
from package import Package
from truck import Truck
import data


def loadpackagedata(HashTable):
    with open("data/Packages.csv") as package_CSV:
        package_data = csv.reader(package_CSV, delimiter=',')
        for package in package_data:
            pid = int(package[0])
            paddress = package[1]
            pcity = package[2]
            pstate = package[3]
            pzip = package[4]
            pdeadline = package[5]
            pkilos = package[6]
            pnotes = package[7]

            p = Package(pid, paddress, pcity, pstate, pzip, pdeadline,
                        pkilos, pnotes)
            HashTable.insert(pid, p)


with open("data/Address.csv") as address_CSV:
    address_data = csv.reader(address_CSV, delimiter=',')
    address_data = list(address_data)




