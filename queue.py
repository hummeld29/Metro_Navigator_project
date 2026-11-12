from linked_list import linked_list

class queue:
    def __init__(self, head, tail):
        self.items = linked_list()
        self.head = head
        self.tail = tail

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return self.items.is_empty()

    def size(self):
        return len(self.items)
    def clear(self):
        self.items = linked_list()
    def __len__(self):
        count = 0
        for _ in self.items:
            count += 1
        return count
    def to_list(self):
        return self.items.to_list()
    def board_passengers():
        pass