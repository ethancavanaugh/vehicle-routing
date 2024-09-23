import csv
from OpenAddressHashTable import OpenAddressHashTable
from Package import Package


# Returns a 2d array with the distance between every address
# Address indexes in this map are retrieved from the addr_index_map
def load_distance_data(dist_csv: str) -> list:
    print("Loading distance data...")
    distance_table = []

    with open(dist_csv, "r", encoding='utf-8-sig') as distance_file:
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

    return distance_table


# Returns a map of package pkg_id -> package object
def load_package_data(pkg_csv: str) -> OpenAddressHashTable:
    print("Loading package data...")
    pkg_map = OpenAddressHashTable()

    with open(pkg_csv, encoding='utf-8-sig') as package_file:
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
            pkg_map[id] = package

    return pkg_map


# Returns a map of addresses to their index in the distance table
def load_address_data(addr_csv: str) -> dict:
    print("Loading address data...")

    addr_map = {}
    with open(addr_csv, encoding='utf-8-sig') as address_file:
        addr_reader = csv.reader(address_file)
        for row in addr_reader:
            addr_map[row[1]] = addr_reader.line_num - 1

    return addr_map
