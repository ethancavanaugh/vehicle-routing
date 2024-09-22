# Ethan Cavanaugh
# Student ID: 010962337

import data_loaders
from RouteFinder import RouteFinder

HUB_ADDRESS = "4001 South 700 East"


if __name__ == '__main__':
    distance_table = distance_table = data_loaders.load_distance_data("WGUPS Distance Table.csv")
    package_map = data_loaders.load_package_data("WGUPS Package Table.csv")
    addr_index_map = data_loaders.load_address_data("WGUPS Address Table.csv")
    route_finder = RouteFinder(distance_table, addr_index_map)

    packages1 = []
    packages2 = []
    for i in range(1, 11):
        packages1.append(package_map[i])
    for i in range(31, 41):
        packages1.append(package_map[i])
    for i in range(21, 31):
        packages2.append(package_map[i])
    for i in range(11, 21):
        packages2.append(package_map[i])

    def pkgs_to_addrs(pkgs):
        addrs = [HUB_ADDRESS]
        for p in pkgs:
            addrs.append(p.address)
        addrs.append(HUB_ADDRESS)
        return addrs

    route_finder.two_opt_tour(pkgs_to_addrs(packages1))
    route_finder.two_opt_tour(pkgs_to_addrs(packages2))
