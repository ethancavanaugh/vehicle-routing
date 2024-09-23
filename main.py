# Ethan Cavanaugh
# Student ID: 010962337

from datetime import *
import dataloaders
from Package import Package
from RouteFinder import RouteFinder
from Truck import Truck

# Dummy package used to represent the hub in each truck's route
HUB = Package(-1, "4001 South 700 East", None, None, None, None, None, "HUB ADDRESS")


if __name__ == '__main__':
    # ************************ LOAD CSV DATA ***************************
    distance_table = distance_table = dataloaders.load_distance_data("WGUPS Distance Table.csv")
    package_map = dataloaders.load_package_data("WGUPS Package Table.csv")
    addr_index_map = dataloaders.load_address_data("WGUPS Address Table.csv")
    route_finder = RouteFinder(distance_table, addr_index_map)

    # ************************ LOAD TRUCKS ***************************
    truck1_package_ids = [1, 2, 6, 21, 22, 25, 26, 28, 29, 31, 32, 33, 40]
    truck2_package_ids = [3, 5, 8, 13, 14, 15, 16, 18, 19, 20, 30, 34, 36, 37, 38, 39]
    truck3_package_ids = [4, 7, 9, 10, 11, 17, 23, 24, 27, 35, 12]

    # Build a list of packages for each truck, adding a dummy hub package to each end for route-finding purposes
    truck1_packages = [HUB] + [package_map[i] for i in truck1_package_ids] + [HUB]
    truck2_packages = [HUB] + [package_map[i] for i in truck2_package_ids] + [HUB]
    truck3_packages = [HUB] + [package_map[i] for i in truck3_package_ids] + [HUB]

    # Run each list of packages through the 2 opt algorithm to minimize the distance travelled
    truck1_packages = route_finder.two_opt_tour(truck1_packages)
    truck2_packages = route_finder.two_opt_tour(truck2_packages)
    truck3_packages = route_finder.two_opt_tour(truck3_packages)

    # Create truck objects
    truck1 = Truck(1, truck1_packages, distance_table, addr_index_map)
    truck2 = Truck(2, truck2_packages, distance_table, addr_index_map)
    truck3 = Truck(3, truck3_packages, distance_table, addr_index_map)

    # Truck 2 departs at 8:00 AM
    truck2_departure_time = datetime.combine(date.today(), time(8))
    truck2.deliver_packages(truck2_departure_time)

    # Truck 1 departs at 9:05 AM because packages 6, 25, 28, and 32 are delayed
    truck1_departure_time = datetime.combine(date.today(), time(9, 5))
    truck1.deliver_packages(truck1_departure_time)

    # Truck 3 departs at 10:20 AM when the address for package 9 is corrected
    truck3_departure_time = datetime.combine(date.today(), time(10, 20))
    truck3.deliver_packages(truck3_departure_time)

    # ************************ USER INTERFACE ***************************
    def print_menu():
        print()
        print("m - Mileage data")
        print("ap - All package statuses")
        print("sp - Single package status")
        print("h - help")
        print("q - Quit")

    # Obtains user inputted time and return it as a time object
    # Returns None if the user wishes to return to previous menu
    def time_input():
        while True:
            try:
                print("Enter a time (hh:mm, 24h format):")
                user_input = input()
                if user_input == 'q':
                    return None
                t = user_input.split(':')
                return time(int(t[0]), int(t[1]))
            except ValueError:
                print("Invalid time entered, enter a valid time or q to return to main menu")

    # Obtains user inputted package id, returning a package object
    # Returns None if the user wishes to return to previous menu
    def package_id_input():
        while True:
            try:
                print("Enter package id:")
                user_input = input()
                if user_input == 'q':
                    return None
                return package_map[int(user_input)]
            except ValueError:
                print("Package id must be an integer, enter a valid id or q to return to main menu")
            except KeyError:
                print("No package exists with that id, enter a valid id or q to return to main menu")

    print()
    print("Welcome to the delivery dashboard, enter an option to continue:", end="")
    print_menu()

    while True:
        print()
        print(":", end="")
        selection = input()

        if selection == 'm':
            print("Truck 1 - %.1f mi | Truck 2 - %.1f mi | Truck 3 - %.1f mi" %
                  (truck1.total_distance, truck2.total_distance, truck3.total_distance))
            print("Total mileage: %.1f mi" % (truck1.total_distance + truck2.total_distance + truck3.total_distance))
        elif selection == "ap":
            status_time = time_input()
            if not status_time: continue

            for pkg in package_map.values():
                print(pkg.get_status(status_time))
        elif selection == 'sp':
            pkg = package_id_input()
            if not pkg: continue
            status_time = time_input()
            if not status_time: continue

            print(pkg.get_status(status_time))
        elif selection == 'h':
            print_menu()
        elif selection == 'q':
            exit(0)
        else:
            print("Invalid selection, enter h to view options")
