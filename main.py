# Ethan Cavanaugh
# Student ID: 010962337

import data_loaders

HUB_ADDRESS = "4001 South 700 East"


def distance_between(addr1, addr2):
    return distance_table[addr_index_map[addr1]][addr_index_map[addr2]]


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
    distance_table = distance_table = data_loaders.load_distance_data("WGUPS Distance Table.csv")
    package_map = data_loaders.load_package_data("WGUPS Package Table.csv")
    addr_index_map = data_loaders.load_address_data("WGUPS Address Table.csv")

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

    two_opt_tour(packages1)
    two_opt_tour(packages2)

