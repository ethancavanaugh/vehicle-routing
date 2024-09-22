import datetime
from Package import *


class Truck:
    AVG_SPEED_MPH = 18

    # Takes a list of package ids and a list of addresses
    def __init__(self, truck_id: int, packages: list[Package], distance_table: list[list[int]], addr_index_map):
        self.id = truck_id
        self.packages = packages
        self.distance_table = distance_table
        self.addr_index_map = addr_index_map

    def deliver_packages(self, departure_time: datetime):
        for p in self.packages:
            p.status = PackageStatus.EN_ROUTE

        cur_time = departure_time
        # Update the time and status for each package that is delivered
        for i in range(1, len(self.packages) - 1):
            package = self.packages[i]
            dist = self.__distance_between(self.packages[i-1], self.packages[i])
            transit_time = datetime.timedelta(hours=(dist / self.AVG_SPEED_MPH))

            cur_time += transit_time
            package.status = PackageStatus.DELIVERED
            package.delivered_time = cur_time

        return_dist = self.__distance_between(self.packages[-2], self.packages[-1])
        cur_time += datetime.timedelta(hours=(return_dist / self.AVG_SPEED_MPH))
        return cur_time

    # Return the distance between two package delivery addresses
    def __distance_between(self, pkg1, pkg2):
        return self.distance_table[self.addr_index_map[pkg1.address]][self.addr_index_map[pkg2.address]]