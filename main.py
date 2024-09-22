# Ethan Cavanaugh
# Student ID: 010962337

from datetime import *
import data_loaders
from Package import Package
from RouteFinder import RouteFinder
from Truck import Truck

# Dummy package used to represent the hub in each truck's route
HUB = Package(-1, "4001 South 700 East", None, None, None, None, None, "HUB ADDRESS")


if __name__ == '__main__':
    # Load all necessary data from csv files
    distance_table = distance_table = data_loaders.load_distance_data("WGUPS Distance Table.csv")
    package_map = data_loaders.load_package_data("WGUPS Package Table.csv")
    addr_index_map = data_loaders.load_address_data("WGUPS Address Table.csv")
    route_finder = RouteFinder(distance_table, addr_index_map)

    truck1_packages = [HUB] + [package_map[i] for i in range(1, 21)] + [HUB]
    truck1_route = route_finder.two_opt_tour(truck1_packages)

    truck2_packages = [HUB] + [package_map[i] for i in range(21, 41)] + [HUB]
    truck2_route = route_finder.two_opt_tour(truck2_packages)

    truck1 = Truck(1, truck1_packages, distance_table, addr_index_map)
    truck2 = Truck(2, truck2_packages, distance_table, addr_index_map)

    truck1_departure_time = datetime.combine(date.today(), time(8))
    truck1.deliver_packages(truck1_departure_time)
    truck2_departure_time = datetime.combine(date.today(), time(8))
    truck2.deliver_packages(truck2_departure_time)

    for i in range(1, 41):
        print(package_map[i])
