# A simple hash table using open addressing
class OpenAddressHashTable:
    INITIAL_SIZE = 16

    def __init__(self):
        self.size = 0  # The current number of items stored in the table
        self.table = []  # Stores a tuple of (key, value) for each item in the table
        for i in range(self.INITIAL_SIZE):
            self.table.append(None)

    def __contains__(self, key):
        try:
            self.__find_index(key)
            return True
        except KeyError:
            return False

    # Adds an item to the hash table
    # If the key already exists in the table, it will be overwritten
    # Resizing occurs if the number of items exceeds half of the table's capacity to reduce collisions
    def __setitem__(self, key, val):
        if key not in self:
            self.size += 1
        if self.size >= len(self.table) // 2:
            self.__resize()
        self.__insert(self.table, key, val)

    # Returns the value of the specified key
    # Raises KeyError if the key is not found
    def __getitem__(self, key):
        i = self.__find_index(key)
        return self.table[i][1]

    # Deletes the item with the specified key
    # The table size will remain the same no matter how many items are removed
    # Raises KeyError if the key is not found
    def __delitem__(self, key):
        i = self.__find_index(key)
        self.table[i] = None
        self.size -= 1

    def __len__(self):
        return self.size

    def values(self):
        values = []
        for item in self.table:
            if item is not None:
                values.append(item[1])
        return values

    # Doubles the capacity of the table and rehashes all existing items
    def __resize(self):
        new_cap = 2 * len(self.table)
        new_table = []
        for i in range(new_cap):
            new_table.append(None)

        # Rehash existing items into new table
        for i in range(len(self.table)):
            if self.table[i]:
                key, val = self.table[i]
                self.__insert(new_table, key, val)

        self.table = new_table

    def __insert(self, table, key, val):
        index = hash(key) % len(table)

        # Loose addressing - increment index until an empty space is found or key is found
        while table[index] and self.table[index][0] != key:
            index = (index + 1) % len(table)

        table[index] = (key, val)

    def __find_index(self, key):
        index = hash(key) % len(self.table)
        while self.table[index] and self.table[index][0] != key:
            index += 1

        #Key is not present if an empty index is found before the key
        if not self.table[index]:
            raise KeyError

        return index
