

class MinHeap:
    def __init__(self):
        self._data = []

    @staticmethod
    def _check_priority(priority):
        if not isinstance(priority, (int, float)):
            raise TypeError("priority must be an int or float")

    def _sift_up(self, i):
        data = self._data
        while i > 0:
            parent = (i - 1) // 2
            if data[i][0] < data[parent][0]:
                data[i], data[parent] = data[parent], data[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        data = self._data
        n = len(data)
        while True:
            smallest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and data[left][0] < data[smallest][0]:
                smallest = left
            if right < n and data[right][0] < data[smallest][0]:
                smallest = right
            if smallest == i:
                break
            data[i], data[smallest] = data[smallest], data[i]
            i = smallest
    def push(self, priority, item):
        self._check_priority(priority)
        self._data.append((priority, item))
        self._sift_up(len(self._data) - 1)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top
    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    @staticmethod
    def build_heap(pairs):
        heap = MinHeap()
        for priority, _ in pairs:
            MinHeap._check_priority(priority)
        heap._data = list(pairs)
        for i in range(len(heap._data) // 2 - 1, -1, -1):
            heap._sift_down(i)
        return heap
    def drain(self):
        result = []
        while self._data:
            result.append(self.pop())
        return result
    def to_list(self):
        return self._data[:]
    def is_valid_heap(self):
        data = self._data
        for i in range(1, len(data)):
            if data[(i - 1) // 2][0] > data[i][0]:
                return False
        return True
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self):
        return len(self._data)