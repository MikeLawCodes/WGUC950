import csv
import hashtable
from package import load_package_data

# Read the package information
with open("data/Packages.csv") as packageCSV:
    packageData = csv.reader(packageCSV)
    packageData = list(packageData)


# code for testing
ht = hashtable.HashTable()
load_package_data("data/Packages.csv", ht)
print(ht)
print(ht.search('18'))
