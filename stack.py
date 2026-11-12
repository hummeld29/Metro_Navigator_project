from linked_list import linked_list


class stack:
    def __init__(self):
        self.linked_list = linked_list()

    def push(self, item):
        self.linked_list.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.linked_list.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.linked_list.peek()

    def is_empty(self):
        return self.linked_list.is_empty()

    def size(self):
        return len(self.linked_list)
    def is_balanced(self, text):
        stack = []
        opening = "({["
        closing = ")}]"
        mapping = {")": "(", "}": "{", "]": "["}

        for char in text:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return len(stack) == 0
    def is_empty(self):
        return len(self.items) == 0
    def clear(self):
        self.items = []
    def __len__(self):
        count = 0
        for _ in self.items:
            count += 1
        return count
    def to_list(self):
        return self.items[:]
    