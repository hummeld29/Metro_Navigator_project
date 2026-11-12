class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size\

    def set(self, key, value):
        index = self._hash(key)
        self.table[index] = value

    def get(self, key, default=None):
        index = self._hash(key)
        return self.table[index] if self.table[index] is not None else default

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = None
    def put(self, key, value):
        index = self._hash(key)
        self.table[index] = value
    def keys(self):
        return [key for key in range(self.size) if self.table[key] is not None]
    def values(self):
        return [value for value in self.table if value is not None]
    def items(self):
        return [(key, self.table[key]) for key in range(self.size) if self.table[key] is not None]
        
    def get_(self, key, default=None):
        index = self._hash(key)
        value = self.table[index]
        return value if value is not None else default
    def __len__(self):
        return sum(1 for x in self.table if x is not None)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)
    def __delitem__(self, key):
        self.delete(key)
    def __contains__(self, key):
        index = self._hash(key)
        return self.table[index] is not None
    def _hash(self, key):
        return hash(key) % self.size
    def load_factor(self):
        return len(self) / self.size
    def remove(self, key):
        index = self._hash(key)
        self.table[index] = None
    def contains(self, key):
        index = self._hash(key)
        return self.table[index] is not None