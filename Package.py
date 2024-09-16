from enum import Enum


class Package:

    def __init__(self, id, address, city, state, zip_code, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = Status.AT_HUB

    def __repr__(self):
        return ("ID:%s Addr: %s, %s, %s %s Deadline: %s Weight: %s Notes: %s Status: %s" %
                (str(self.id), self.address, self.city, self.state, self.zip_code,
                 self.deadline, str(self.weight), self.notes, str(self.status)))


class Status(Enum):
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3
