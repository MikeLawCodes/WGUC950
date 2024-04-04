# Name: Michael Lawrence
# Email: Mlaw101@wgu.edu
# Student ID: 002680987

import datetime
from distance import get_distance
from hashtable import HashTable
from load_csv import load_distance_data, load_address_data, load_package_data
import truck

# load data into variables and hash table using functions from load_csv
address_data = load_address_data()
distance_data = load_distance_data()
package_hash_table = HashTable()
load_package_data("data/Packages.csv", package_hash_table)

# TODO Delete this test code when finished with project
# print(package_hash_table.lookup('1'))
#
# print(address_data)
#
# print(get_distance(2, 6))
# print(get_distance("1330 2100 S", "2010 W 500 S"))
# print(get_distance("2010 W 500 S", "1330 2100 S"))

first_truck = truck.Truck(1, datetime.timedelta(hours=8))
first_truck.packages_on_truck = [13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 35, 37, 40]

second_truck = truck.Truck(2, datetime.timedelta(hours=10, minutes=20))
second_truck.packages_on_truck = [2, 3, 12, 17, 18, 21, 22, 23, 24, 28, 32, 36, 38, 39]

third_truck = truck.Truck(3, datetime.timedelta(hours=9, minutes=5))
third_truck.packages_on_truck = [1, 4, 5, 6, 7, 8, 9, 10, 11, 25, 26, 27, 28, 33, 35]


def package_delivery(truck_object):
    not_delivered = []
    for package_id in truck_object.packages_on_truck:
        package = package_hash_table.lookup(package_id)
        # print(package)
        not_delivered.append(package)
    truck_object.packages_on_truck.clear()

    while len(not_delivered) > 0:
        # using min function with key parameter to get the package with smaller distance.
        next_package = min(not_delivered,
                           key=lambda package: get_distance(truck_object.truck_address, package.package_address))
        next_address = get_distance(truck_object.truck_address, next_package.package_address)

        truck_object.packages_on_truck.append(next_package.package_id)
        not_delivered.remove(next_package)
        truck_object.mileage += next_address
        truck_object.truck_address = next_package.package_address
        truck_object.curr_time += datetime.timedelta(hours=next_address / truck_object.speed)
        next_package.arrival_time = truck_object.curr_time
        next_package.departure_time = truck_object.departure_time


package_delivery(first_truck)
package_delivery(second_truck)
third_truck.departure_time = min(first_truck.curr_time, second_truck.curr_time)
package_delivery(third_truck)


class Main:
    # User Interface
    # Upon running the program, the below message will appear.
    print("Western Governors University Parcel Service (WGUPS)")
    print("The mileage for the route is:")
    print(first_truck.mileage + second_truck.mileage + third_truck.mileage)  # Print total mileage for all trucks
    # The user will be asked to start the process by entering the word "time"
    text = input("To start please type the word 'time' (All else will cause the program to quit).")
    # If the user doesn't type "leave" the program will ask for a specific time in regard to checking packages
    if text == "time":
        try:
            # The user will be asked to enter a specific time
            user_time = input("Please enter a time to check status of package(s). Use the following format, HH:MM:SS")
            (h, m, s) = user_time.split(":")
            # TODO Change this function
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # The user will be asked if they want to see the status of all packages or only one
            second_input = input("To view the status of an individual package please type 'solo'. For a rundown of all"
                                 " packages please type 'all'.")
            # If the user enters "solo" the program will ask for one package ID
            if second_input == "solo":
                try:
                    # The user will be asked to input a package ID. Invalid entry will cause the program to quit
                    solo_input = input("Enter the numeric package ID")
                    package = package_hash_table.lookup(int(solo_input))
                    package.update_status(convert_timedelta)
                    print(str(package))
                except ValueError:
                    print("Entry invalid. Closing program.")
                    exit()
            # If the user types "all" the program will display all package information at once
            elif second_input == "all":
                try:
                    for packageID in range(1, 41):
                        package = package_hash_table.lookup(packageID)
                        package.update_status(convert_timedelta)
                        print(str(package))
                except ValueError:
                    print("Entry invalid. Closing program.")
                    exit()
            else:
                exit()
        except ValueError:
            print("Entry invalid. Closing program.")
            exit()
    elif input != "time":
        print("Entry invalid. Closing program.")
        exit()
