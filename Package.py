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
        self.delivered_time = None

    def __repr__(self):
        return ("ID:%s Addr: %s, %s, %s %s Deadline: %s Weight: %s Notes: %s Status: %s" %
                (str(self.pkg_id), self.address, self.city, self.state, self.zip_code,
                 self.deadline, str(self.weight), self.notes,
                 (str(self.status) if self.status is not PackageStatus.DELIVERED
                  else "Delivered at " + str(self.delivered_time))))


class PackageStatus(Enum):
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3
