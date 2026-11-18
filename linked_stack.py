from linked_list import LinkedList


class Stack:
    def __init__(self):
        self._list = LinkedList()

    def push(self, item):
        self._list.prepend(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self._list.head.value
        self._list.remove_at(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._list.head.value

    def is_empty(self):
        return self._list.head is None

    def size(self):
        return len(self)

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
        return self._list.to_list()


def is_balanced(text):
    if not isinstance(text, str):
        raise TypeError("is_balanced expects a string")

    pairs = {'(': ')', '{': '}', '[': ']'}
    closers = set(pairs.values())
    stack = Stack()

    for char in text:
        if char in pairs:
            stack.push(char)
        elif char in closers:
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False
    return stack.is_empty()