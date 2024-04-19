# Name: Michael Lawrence
# Email: Mlaw101@wgu.edu
# Student ID: 002680987

import datetime
from distance import get_distance
from hashtable import HashTable
from load_csv import load_distance_data, load_address_data, load_package_data
import truck

# Call functions to load data into variables and hash table using functions from load_csv.py
address_data = load_address_data()
distance_data = load_distance_data()
package_hash_table = HashTable()  # Initialise Hash Table for package information.
load_package_data("data/Packages.csv", package_hash_table)  # Load package data into hash table.

# Create truck objects and load them with packages according to restrictions.
first_truck = truck.Truck("Truck 1", datetime.timedelta(hours=8))
# List of package ID's to be loaded onto the first truck.
first_truck.packages_on_truck = [13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 35, 37, 40]

second_truck = truck.Truck("Truck 2", datetime.timedelta(hours=10, minutes=10))
# List of package ID's to be loaded onto the second truck.
second_truck.packages_on_truck = [2, 3, 9, 12, 17, 18, 21, 22, 23, 24, 28, 32, 36, 38, 39]

third_truck = truck.Truck("Truck 3", datetime.timedelta(hours=9, minutes=5))
# List of package ID's to be loaded onto the third truck
third_truck.packages_on_truck = [1, 4, 5, 6, 7, 8, 10, 11, 25, 26, 27, 28, 33, 35]


def package_delivery(truck_object):
    not_delivered = []
    for package_id in truck_object.packages_on_truck:
        package = package_hash_table.lookup(package_id)
        # Checks the time for wrong address update
        if package_id == 9 and truck_object.curr_time >= datetime.timedelta(hours=10, minutes=20):
            package.package_address = "410 S State St"
            package.city = "Salt Lake City"
            package.zipcode = "84111"
        package.truck_id = truck_object.truck_id
        not_delivered.append(package)
    truck_object.packages_on_truck.clear()

    while len(not_delivered) > 0:
        # using min function with key parameter to get the package with smaller distance
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
    print("----------------------------------------------------------------------------------------"
          "----------------------------------------------------------------------------------------"
          "------------------------------------------------------------")
    print("WESTERN GOVERNORS UNIVERSITY PARCEL SERVICE ")
    print("----------------------------------------------------------------------------------------"
          "----------------------------------------------------------------------------------------"
          "------------------------------------------------------------")
    print(f"{'Package ID':11} | {'Delivery Address':39} | {'City':16} | {'State':6} "
          f"| {'Zip':5} | {'Deadline':9} | {'Kilos':6} | {'Truck ID':9} | {'Status':10} "
          f"| {'Departure Time':15} | {'Arrival Time':12} | {'Special Notes':59}")
    EOD = datetime.timedelta(hours=24, minutes=59)
    for packageID in range(1, 40):
        package = package_hash_table.lookup(packageID)
        package.update_status(EOD)
        print("----------------------------------------------------------------------------------------"
              "----------------------------------------------------------------------------------------"
              "------------------------------------------------------------")
        print(str(package))
        print("----------------------------------------------------------------------------------------"
              "----------------------------------------------------------------------------------------"
              "------------------------------------------------------------")
    print("The above chart displays all package statuses at end-of-day (EOD)\n")
    print("The total mileage for the route is:\n")
    print(first_truck.mileage + second_truck.mileage + third_truck.mileage)
    print("----------------------------------------------------------------------------------------"
          "----------------------------------------------------------------------------------------"
          "------------------------------------------------------------")
    user_input = input("To check status at specific time, type [Y] for yes or [N] for no and to exit the program\n")
    if user_input == "Y":
        try:
            user_time = input("Enter a time in HH:MM:SS format\n")
            (hour, minute, second) = user_time.split(":")  # splits the users input into usable variables
            converted_time_input = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
            user_input = input("To view an individual package's status, type the package ID [1-40],\n"
                               "or type [ALL] to view all package statuses\n")
            # If the user enters "solo" the program will ask for one package ID
            if user_input.isdigit() and int(user_input) in range(1, 40):
                try:
                    package_id_request = user_input
                    package = package_hash_table.lookup(int(package_id_request))
                    package.update_status(converted_time_input)
                    print("----------------------------------------------------------------------------------------"
                          "----------------------------------------------------------------------------------------"
                          "------------------------------------------------------------")
                    print(str(package))
                    print("----------------------------------------------------------------------------------------"
                          "----------------------------------------------------------------------------------------"
                          "------------------------------------------------------------")
                except ValueError:
                    print("Invalid Input. Please rerun the program and enter an integer within range (1-40)\n")
                    exit()
            # If the user types "all" the program will display all package information at once
            elif user_input == "ALL":
                try:
                    print("----------------------------------------------------------------------------------------"
                          "----------------------------------------------------------------------------------------"
                          "------------------------------------------------------------")
                    print("WESTERN GOVERNORS UNIVERSITY PARCEL SERVICE ")
                    print("----------------------------------------------------------------------------------------"
                          "----------------------------------------------------------------------------------------"
                          "------------------------------------------------------------")
                    print(f"{'Package ID':11} | {'Delivery Address':39} | {'City':16} | {'State':6} "
                          f"| {'Zip':5} | {'Deadline':9} | {'Kilos':6} | {'Truck ID':9} | {'Status':10} "
                          f"| {'Departure Time':15} | {'Arrival Time':12} | {'Special Notes':59}")
                    for package_id in range(1, 40):
                        package = package_hash_table.lookup(package_id)
                        package.update_status(converted_time_input)
                        print("----------------------------------------------------------------------------------------"
                              "----------------------------------------------------------------------------------------"
                              "------------------------------------------------------------")
                        print(str(package))
                except ValueError:
                    print("Please note, input is case sensitive. Please rerun the program and "
                          "type [ALL] to view all package statuses\n")
                    exit()
            else:
                exit()
        except ValueError:
            print("Invalid Time. Please rerun program and enter a valid time in HH:MM:SS format\n")
            exit()
    elif input != "N":
        print("Program Closed.\nThank you for using WGUPS.")
        exit()
