from datetime import *
from enum import Enum


class Package:

    def __init__(self, pkg_id, address, city, state, zip_code, deadline, weight, notes):
        self.pkg_id = pkg_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = PackageStatus.AT_HUB
        self.departure_time = None
        self.truck_id = None
        self.delivered_time = None

    def __repr__(self):
        return ("ID:%s Addr: %s, %s, %s %s Deadline: %s Weight: %s Notes: %s" %
                (str(self.pkg_id), self.address, self.city, self.state, self.zip_code,
                 self.deadline, str(self.weight), self.notes))

    def get_status(self, status_time=datetime.max):
        if isinstance(status_time, time):
            status_time = datetime.combine(date.today(), status_time)
        if not isinstance(status_time, datetime):
            raise TypeError

        if self.delivered_time and status_time >= self.delivered_time:
            status = "Delivered by truck " + str(self.truck_id) + " at " + str(self.delivered_time)
        elif self.departure_time and status_time >= self.departure_time:
            status = "Out for delivery on truck " + str(self.truck_id) + " at " + str(self.departure_time)
        else:
            status = "At hub"
        return self.__repr__() + " Status: " + status


class PackageStatus(Enum):
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3
