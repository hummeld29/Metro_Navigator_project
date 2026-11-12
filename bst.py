class treeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class bst: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = bst(key, value)
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = bst(key, value)
            else:
                self.right.insert(key, value)
    def contains(self, key):
        if key == self.key:
            return True
        elif key < self.key and self.left is not None:
            return self.left.contains(key)
        elif key > self.key and self.right is not None:
            return self.right.contains(key)
        return False
    def get(self, key):
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.get(key)
        elif key > self.key and self.right is not None:
            return self.right.get(key)
        return None
    def delete(self, key):
        if key < self.key:
            if self.left is not None:
                self.left = self.left.delete(key)
        elif key > self.key:
            if self.right is not None:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_larger_node = self.right
                while min_larger_node.left is not None:
                    min_larger_node = min_larger_node.left
                self.key = min_larger_node.key
                self.value = min_larger_node.value
                self.right = self.right.delete(min_larger_node.key)
        return self
    def inorder(self):
        elements = []
        if self.left is not None:
            elements += self.left.inorder()
        elements.append(self.key)
        if self.right is not None:
            elements += self.right.inorder()
        return elements
    def preorder(self):
        elements = [self.key]
        if self.left is not None:
            elements += self.left.preorder()
        if self.right is not None:
            elements += self.right.preorder()
        return elements
    def postorder(self):
        elements = []
        if self.left is not None:
            elements += self.left.postorder()
        if self.right is not None:
            elements += self.right.postorder()
        elements.append(self.key)
        return elements
    def level_order(self):
        elements = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            elements.append(current.key)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return elements
    def height(self):
        left_height = self.left.height() if self.left is not None else 0
        right_height = self.right.height() if self.right is not None else 0
        return 1 + max(left_height, right_height)
    def min_key(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.key
    def max_key(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.key
    def count_leaves(self):
        if self.left is None and self.right is None:
            return 1
        left_leaves = self.left.count_leaves() if self.left is not None else 0
        right_leaves = self.right.count_leaves() if self.right is not None else 0
        return left_leaves + right_leaves
    def range_query(self, low, high): 
        elements = []
        if self.left is not None:
            elements += self.left.range_query(low, high)
        if low <= self.key <= high:
            elements.append(self.key)
        if self.right is not None:
            elements += self.right.range_query(low, high)
        return elements
    def is_valid_bst(self, min_key=float('-inf'), max_key=float('inf')):
        if not (min_key < self.key < max_key):
            return False
        left_is_valid = self.left.is_valid_bst(min_key, self.key) if self.left is not None else True
        right_is_valid = self.right.is_valid_bst(self.key, max_key) if self.right is not None else True
        return left_is_valid and right_is_valid
    def is_empty(self):
        return self is None
    def len(self):
        left_count = self.left.len() if self.left is not None else 0
        right_count = self.right.len() if self.right is not None else 0
        return 1 + left_count + right_count     

    def search(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        return False

    def inorder_traversal(self):
        elements = []
        if self.left is not None:
            elements += self.left.inorder_traversal()
        elements.append(self.value)
        if self.right is not None:
            elements += self.right.inorder_traversal()
        return elements
    