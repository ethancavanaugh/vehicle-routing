class RouteFinder:
    def __init__(self, distance_table, addr_index_map):
        self.distance_table = distance_table
        self.addr_index_map = addr_index_map

    # Find a locally optimal tour, operating on the addresses between start(inclusive) and end(exclusive)
    def two_opt_tour(self, tour, start=0, end=None):
        if end is None:
            end = len(tour)

        # Calculate initial tour length
        length = 0
        for i in range(start + 1, end):
            length += self.__distance_between(tour[i], tour[i-1])
        print(tour)
        print(length)

        # Test each possible swap of two edges, making any improving swap
        improved = True
        while improved:
            improved = False
            for v1 in range(start, end - 2):
                for v2 in range(v1 + 1, end - 1):
                    swap_difference = self.__get_swap_difference(tour, v1, v2)
                    if swap_difference < 0:
                        improved = True
                        length += swap_difference
                        tour = self.__swap_edges(tour, v1, v2)
    
        print(tour)
        print(length)

    def __distance_between(self, addr1, addr2):
        return self.distance_table[self.addr_index_map[addr1]][self.addr_index_map[addr2]]

    # Returns the change in tour length if the edges starting at v1 and v2 are swapped
    def __get_swap_difference(self, tour, v1, v2):
        cur_dist = self.__distance_between(tour[v1], tour[v1 + 1]) + self.__distance_between(tour[v2], tour[v2 + 1])
        new_dist = self.__distance_between(tour[v1], tour[v2]) + self.__distance_between(tour[v1 + 1], tour[v2 + 1])
        return new_dist - cur_dist

    def __swap_edges(self, tour, v1, v2):
        new_tour = tour[:v1 + 1]
        for i in range(v2, v1, -1):
            new_tour.append(tour[i])
        new_tour.extend(tour[v2 + 1:])
        return new_tour
