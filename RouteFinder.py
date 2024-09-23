from Package import Package


class RouteFinder:
    def __init__(self, distance_table, addr_index_map):
        self.distance_table = distance_table
        self.addr_index_map = addr_index_map

    # Find a locally optimal tour from a list of packages
    # Operates on the packages between start(inclusive) and end(exclusive)
    def two_opt_tour(self, packages: list[Package], start=0, end=None):
        if end is None:
            end = len(packages)

        # Calculate initial tour length
        length = 0
        for i in range(start + 1, end):
            length += self.__distance_between(packages[i], packages[i-1])
        init_length = length

        # Test each possible swap of two edges, making any improving swap
        improved = True
        while improved:
            improved = False
            for v1 in range(start, end - 2):
                for v2 in range(v1 + 1, end - 1):
                    swap_difference = self.__get_swap_difference(packages, v1, v2)
                    if swap_difference < 0:
                        improved = True
                        length += swap_difference
                        packages = self.__swap_edges(packages, v1, v2)
    
        print("2-opt algorithm complete, reduced distance from %.1f mi to %.1f mi!" % (init_length, length))
        return packages

    # Return the distance between two package delivery addresses
    def __distance_between(self, pkg1, pkg2):
        return self.distance_table[self.addr_index_map[pkg1.address]][self.addr_index_map[pkg2.address]]

    # Returns the change in tour length if the edges starting at v1 and v2 are swapped
    def __get_swap_difference(self, tour, v1, v2):
        cur_dist = self.__distance_between(tour[v1], tour[v1 + 1]) + self.__distance_between(tour[v2], tour[v2 + 1])
        new_dist = self.__distance_between(tour[v1], tour[v2]) + self.__distance_between(tour[v1 + 1], tour[v2 + 1])
        return new_dist - cur_dist

    # Swaps the edges beginning at v1 and v2
    def __swap_edges(self, tour, v1, v2):
        new_tour = tour[:v1 + 1]
        for i in range(v2, v1, -1):
            new_tour.append(tour[i])
        new_tour.extend(tour[v2 + 1:])
        return new_tour
