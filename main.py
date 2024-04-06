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

# Create truck objects and load them with packages according to restrictions
first_truck = truck.Truck("Truck 1", datetime.timedelta(hours=8))
first_truck.packages_on_truck = [13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 35, 37, 40]

second_truck = truck.Truck("Truck 2", datetime.timedelta(hours=10, minutes=20))
second_truck.packages_on_truck = [2, 3, 12, 17, 18, 21, 22, 23, 24, 28, 32, 36, 38, 39]

third_truck = truck.Truck("Truck 3", datetime.timedelta(hours=9, minutes=5))
third_truck.packages_on_truck = [1, 4, 5, 6, 7, 8, 9, 10, 11, 25, 26, 27, 28, 33, 35]


def package_delivery(truck_object):
    not_delivered = []
    for package_id in truck_object.packages_on_truck:
        package = package_hash_table.lookup(package_id)
        if package_id == 9:
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


# TODO Reformat the main class for better UX

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
    user_input = input("To check status at specific time type [Y] for yes or [N] for no and to exit the program\n")
    if user_input == "Y":
        try:
            user_time = input("Please enter a time to check status of package(s). Use the following format, HH:MM:SS\n")
            (h, m, s) = user_time.split(":")
            converted_time_input = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # The user will be asked if they want to see the status of all packages or only one
            user_input = input("To view the status of an individual package please type 'solo'. For a rundown of all"
                               " packages please type 'all' ")
            # If the user enters "solo" the program will ask for one package ID
            if user_input == "solo":
                try:
                    # The user will be asked to input a package ID. Invalid entry will cause the program to quit
                    package_id_request = input("Please enter Package ID number\n")
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
                    print("Entry invalid. Closing program.")
                    exit()
            # If the user types "all" the program will display all package information at once
            elif user_input == "all":
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
                    for packageID in range(1, 40):
                        package = package_hash_table.lookup(packageID)
                        package.update_status(converted_time_input)
                        print("----------------------------------------------------------------------------------------"
                              "----------------------------------------------------------------------------------------"
                              "------------------------------------------------------------")
                        print(str(package))
                except ValueError:
                    print("Entry invalid. Closing program.")
                    exit()
            else:
                exit()
        except ValueError:
            print("Entry invalid. Closing program.")
            exit()
    elif input != "N":
        print("Program Closed.\nThank you for using WGUPS.")
        exit()
