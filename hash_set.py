from hash_table import HashTable

class HashSet:
    def __init__(self):
        self.table = HashTable()

    def add(self, key):
        if self.contains(key):
            return False
        self.table.put(key, True)
        return True

    def remove(self, key):
        self.table.remove(key)

    def contains(self, key):
        return self.table.contains(key)

    def __len__(self):
        return len(self.table)
    def __contains__(self, key):
        return self.contains(key)
    def is_empty(self):
        return len(self) == 0
    def clear(self):
        self.table = HashTable()
    def to_list(self):
        return list(self.table.keys())
    def __iter__(self):
        for key in self.table.keys():
            yield key
    def intersection(self, other):
        self._check_other(other)
        result = HashSet()
        for key in self.to_list():
            if other.contains(key):
                result.add(key)
        return result
    def union(self, other):
        self._check_other(other)
        result = HashSet()
        for key in self.to_list():
            result.add(key)
        for key in other.to_list():
            result.add(key)
        return result

    
    def __str__(self):
        return f"HashSet({self.to_list()})"

    def discard(self, key):
        if self.contains(key):
            self.remove(key)
            return True
        return False
    def difference(self, other):
        self._check_other(other)
        result = HashSet()
        for key in self.to_list():
            if not other.contains(key):
                result.add(key)
        return result
    def symmetric_difference(self, other):
        self._check_other(other)
        result = HashSet()
        for key in self.to_list():
            if not other.contains(key):
                result.add(key)
        for key in other.to_list():
            if not self.contains(key):
                result.add(key)
        return result
    def is_subset(self, other):
        self._check_other(other)
        for key in self.to_list():
            if not other.contains(key):
                return False
        return True
    def _check_other(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Argument must be a HashSet")
    
    

