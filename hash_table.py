class _HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.table = [None] * capacity
        self._len = 0

    def _hash(self, key):
        self._check_key(key)
        h = 0
        for i, char in enumerate(key):
            h = (h * 31 + ord(char) * (i + 1)) % self.capacity
        return h
    def _check_key(self, key):
        if not isinstance(key, str):
            raise TypeError("key must be a string")

    def set(self, key, value):
        self.put(key, value)

    def put(self, key, value):
        self._check_key(key)
        index = self._hash(key)
        curr = self.table[index]
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        new_node = _HashNode(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self._len += 1
        if self.load_factor() > 0.75:
            self._resize()
    def keys(self):
        result = []
        for node in self.table:
            while node is not None:
                result.append(node.key)
                node = node.next
        return result

    def values(self):
        result = []
        for node in self.table:
            while node is not None:
                result.append(node.value)
                node = node.next
        return result

    def items(self):
        result = []
        for node in self.table:
            while node is not None:
                result.append((node.key, node.value))
                node = node.next
        return result

    def get(self, key, default=None):
        self._check_key(key)
        index = self._hash(key)
        curr = self.table[index]
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return default

    def __len__(self):
        return self._len

    def __getitem__(self, key):
        self._check_key(key)
        index = self._hash(key)
        curr = self.table[index]
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        raise KeyError(f"Key '{key}' not found in HashTable")

    def __setitem__(self, key, value):
        self.set(key, value)
    def __delitem__(self, key):
        self.delete(key)
    def __contains__(self, key):
        index = self._hash(key)
        return self.table[index] is not None

    def load_factor(self):
        return self._len / self.capacity
    def remove(self, key):
        self._check_key(key)
        index = self._hash(key)
        curr = self.table[index]
        prev = None
        while curr is not None:
            if curr.key == key:
                if prev is None:
                    self.table[index] = curr.next
                else:
                    prev.next = curr.next
                self._len -= 1
                return curr.value
            prev = curr
            curr = curr.next
        raise KeyError(f"Key '{key}' not found in HashTable")

    def contains(self, key):
        index = self._hash(key)
        curr = self.table[index]
        while curr is not None:
            if curr.key == key:
                return True
            curr = curr.next
        return False

    def _resize(self,):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self._len = 0
        for node in old_table:
            curr = node
            while curr is not None:
                self.put(curr.key, curr.value)
                curr = curr.next
    def __contains__(self, key):
        return self.contains(key)
    
    