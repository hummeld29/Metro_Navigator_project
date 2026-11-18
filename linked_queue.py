from linked_list import LinkedList

class Queue:
    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._list.get(0)
        self._list.remove_at(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._list.head.value
    def is_empty(self):
        return self._list.head is None

    def clear(self):
        self._list = LinkedList()
    def __len__(self):
        count = 0
        current = self._list.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def to_list(self):
        items = []
        current = self._list.head
        while current is not None:
            items.append(current.value)
            current = current.next
        return items
    
    
def hot_potato(names, k):
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError("k must be an integer")
    if len(names) == 0 or k < 1:
        raise ValueError("need at least one name and k >= 1")
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    eliminated = []
    remaining = len(names)
    while remaining > 1:
        for _ in range((k - 1) % remaining):
            queue.enqueue(queue.dequeue())
        eliminated.append(queue.dequeue())
        remaining -= 1
    return eliminated, queue.dequeue()
def board_passengers( seats_available, names):
    if not isinstance(seats_available, int) or isinstance(seats_available, bool):
        raise TypeError("seats_available must be an integer")
    if seats_available < 0:
        raise ValueError("seats_available can't be negative")
    q = Queue()
    for name in names:
        q.enqueue(name)
    boarded = []
    while seats_available > 0 and not q.is_empty():
        boarded.append(q.dequeue())
        seats_available -= 1
    return boarded, q.to_list()