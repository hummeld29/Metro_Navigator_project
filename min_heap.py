

class min_heap:
    def __init__(self, _data=None):
        self.heap = _data if _data is not None else []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    def push(self, priority, item):
        self.insert((priority, item))
    def pop(self):
        return self.extract_min()
    def peek(self):
        return self.heap[0] if self.heap else None
    @staticmethod
    def build_heap(pairs):
        heap = min_heap()
        for priority, item in pairs:
            heap.insert((priority, item))
        return heap

    def drain(self):
        while self.heap:
            yield self.extract_min()
    def to_list(self):
        return self.heap[:]
    def is_valid_heap(self):
        for i in range(len(self.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self.heap) and self.heap[left] < self.heap[i]:
                return False
            if right < len(self.heap) and self.heap[right] < self.heap[i]:
                return False
        return True
    def is_empty(self):
        return len(self.heap) == 0
    def __len__(self):
        return len(self.heap)
    