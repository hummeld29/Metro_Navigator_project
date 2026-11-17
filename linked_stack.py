from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, item):
        self.linked_list.prepend(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self.linked_list.head.value
        self.linked_list.remove_at(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.linked_list.head.value

    def is_empty(self):
        return self.linked_list is None 

    def size(self):
        return len(self.linked_list)
    
    def is_balanced(self, text):
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for char in text:
            if char in pairs:
                stack.append(char)
            elif char in pairs.values():
                if not stack or pairs[stack.pop()] != char:
                    return False
        return stack.is_empty()

        
    def is_empty(self):
        return self.linked_list.head is None
    def clear(self):
        self._list = LinkedList()
    def __len__(self):
        count = 0
        current = self.linked_list.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def to_list(self):
        return self.linked_list.to_list()
    