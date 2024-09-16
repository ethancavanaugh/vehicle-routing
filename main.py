# Ethan Cavanaugh
# Student ID: 010962337

from OpenAddressHashTable import OpenAddressHashTable
from Package import Package
import csv

PACKAGE_CSV = "WGUPS Package File.csv"
ADDRESS_CSV = "WGUPS Address Table.csv"
DISTANCE_CSV = "WGUPS Distance Table.csv"
HUB_ADDRESS = "4001 South 700 East"

def load_package_data():
    print("Loading package data...")

    with open(PACKAGE_CSV, encoding='utf-8-sig') as package_file:
        package_reader = csv.reader(package_file)
        next(package_reader)  # Skip header
        for row in package_reader:
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = int(row[6])
            notes = row[7]

            package = Package(id, address, city, state, zip_code, deadline, weight, notes)
            package_map[id] = package


def load_address_data():
    print("Loading address data...")

    with open(ADDRESS_CSV, encoding='utf-8-sig') as address_file:
        addr_reader = csv.reader(address_file)
        for row in addr_reader:
            address_index_map[row[1]] = addr_reader.line_num - 1


def load_distance_data():
    print("Loading distance data...")

    with open(DISTANCE_CSV, "r", encoding='utf-8-sig') as distance_file:
        dist_reader = csv.reader(distance_file, delimiter=',')
        for reader_row in dist_reader:
            row = []
            for dist in reader_row:
                row.append(float(dist)) if dist != '' else float('inf')
            distance_table.append(row)

    # Fill in the rest of the table, mirroring the distances since the csv file only shows one direction
    # i.e. distance from b->a = a->b
    for i in range(len(distance_table)):
        for j in range(i + 1, len(distance_table)):
            distance_table[i].append(distance_table[j][i])


def distance_between(addr1, addr2):
    return distance_table[address_index_map[addr1]][address_index_map[addr2]]


def get_swap_difference(tour, v1, v2):
    cur_dist = distance_between(tour[v1], tour[v1 + 1]) + distance_between(tour[v2], tour[v2 + 1])
    new_dist = distance_between(tour[v1], tour[v2]) + distance_between(tour[v1 + 1], tour[v2 + 1])
    return new_dist - cur_dist


def swapped_edges(tour, v1, v2):
    new_tour = tour[:v1 + 1]
    for i in range(v2, v1, -1):
        new_tour.append(tour[i])
    new_tour.extend(tour[v2 + 1:])
    return new_tour
        


def two_opt_tour(packages):
    tour = [HUB_ADDRESS]
    length = 0
    for package in packages:
        tour.append(package.address)
        length += distance_between(tour[-1], tour[-2])
    tour.append(HUB_ADDRESS)
    length += distance_between(tour[-1], tour[-2])
    print(tour)
    print(length)

    improved = True
    while improved:
        improved = False
        for v1 in range(len(tour) - 2):
            for v2 in range(v1 + 1, len(tour) - 1):
                swap_difference = get_swap_difference(tour, v1, v2)
                if swap_difference < 0:
                    improved = True
                    length += swap_difference
                    tour = swapped_edges(tour, v1, v2)

    print(tour)
    print(length)


if __name__ == '__main__':
    package_map = OpenAddressHashTable()  # Maps package id -> Package object
    address_index_map = {}  # Maps address string -> index in distance table
    distance_table = []

    load_package_data()
    load_address_data()
    load_distance_data()

    packages = []
    for i in range(1, 40):
        packages.append(package_map[i])

    two_opt_tour(packages)

