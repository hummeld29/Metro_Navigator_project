class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def remove(self, value):
        current = self.head
        previous = None
        
        while current is not None:
            if current.value == value:
                if previous is None:  
                    self.head = current.next
                    if self.head is None:  
                        self.tail = None
                else:
                    previous.next = current.next
                    if previous.next is None:  
                        self.tail = previous
                self.size -= 1
                return True
                
            previous = current
            current = current.next
            
        return False

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
            
        if index == 0:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return removed_value
            
        current = self.head
        for _ in range(index - 1):
            current = current.next
            
        removed_value = current.next.value
        current.next = current.next.next
        
        if current.next is None:  
            self.tail = current
            
        self.size -= 1
        return removed_value

    def reverse(self):
        previous = None
        current = self.head
        self.tail = self.head 
        
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            
        self.head = previous  

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def to_list(self):
        return list(self)  

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        if self.is_empty():
            return "None"
        parts = [str(x) for x in self]
        parts.append("None")
        return " -> ".join(parts) + " -> None"