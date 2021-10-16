import collections


class LruCache:
    def __init__(self, capacity):

        if capacity is None:
            self.capacity = 1
        elif capacity > 3000:
            self.capacity = 3000
        else:
            self.capacity = capacity
        self.cache_table = collections.OrderedDict()

    def get(self, key) -> int:

        if key in self.cache_table:
            value = self.cache_table.pop(key)
            self.cache_table[key] = value
            return value

        return -1

    def put(self, key, value) -> None:

        if value is None:
            return

        if key in self.cache_table:
            self.cache_table.pop(key)
        self.cache_table[key] = value

        if len(self.cache_table) > self.capacity:
            self.cache_table.popitem(last=False)
