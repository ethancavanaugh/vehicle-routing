# Ethan Cavanaugh
# Student ID: 010962337

from OpenAddressHashTable import OpenAddressHashTable
from Package import Package
import csv

PACKAGE_CSV = "WGUPS Package File.csv"
ADDRESS_CSV = "WGUPS Address Table.csv"
DISTANCE_CSV = "WGUPS Distance Table.csv"


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
            package_map.add(id, package)


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


if __name__ == '__main__':
    package_map = OpenAddressHashTable()  # Maps package id -> Package object
    address_index_map = {}  # Maps address string -> index in distance table
    distance_table = []

    load_package_data()
    load_address_data()
    load_distance_data()

    p1 = package_map.get(2)
    p2 = package_map.get(5)

    print(p1)
    print(p2)

    print(distance_between(p1.address, p2.address))

