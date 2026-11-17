
from collections import deque


class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self._size = 0
    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _find(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None

    def contains(self, key):
        return self._find(key) is not None

    def get(self, key):
        node = self._find(key)
        if node is None:
            raise KeyError(key)
        return node.value
    def insert(self, key, value=None):
        if self.root is None:
            self.root = TreeNode(key, value)
            self._size = 1
            return
        node = self.root
        while True:
            if key == node.key:
                node.value = value  
                return
            if key < node.key:
                if node.left is None:
                    node.left = TreeNode(key, value)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(key, value)
                    break
                node = node.right
        self._size += 1

    def delete(self, key):
        parent = None
        node = self.root
        while node is not None and node.key != key:
            parent = node
            node = node.left if key < node.key else node.right
        if node is None:
            return False
        if node.left is not None and node.right is not None:
            succ_parent = node
            succ = node.right
            while succ.left is not None:
                succ_parent = succ
                succ = succ.left
            node.key, node.value = succ.key, succ.value
            parent, node = succ_parent, succ

        # Now node has at most one child.
        child = node.left if node.left is not None else node.right
        if parent is None:
            self.root = child
        elif parent.left is node:
            parent.left = child
        else:
            parent.right = child
        self._size -= 1
        return True
    def inorder(self):
        result, stack, node = [], [], self.root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.key)
            node = node.right
        return result

    def preorder(self):
        result = []
        if self.root is None:
            return result
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    def postorder(self):
        result = []
        if self.root is None:
            return result
        stack = [self.root]
        while stack:  
            node = stack.pop()
            result.append(node.key)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        result.reverse()
        return result

    def level_order(self):
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result
    def height(self):
        if self.root is None:
            return 0
        h = 0
        level = [self.root]
        while level:
            h += 1
            nxt = []
            for node in level:
                if node.left is not None:
                    nxt.append(node.left)
                if node.right is not None:
                    nxt.append(node.right)
            level = nxt
        return h

    def min_key(self):
        if self.root is None:
            raise ValueError("tree is empty")
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def max_key(self):
        if self.root is None:
            raise ValueError("tree is empty")
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    def count_leaves(self):
        if self.root is None:
            return 0
        count, stack = 0, [self.root]
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                count += 1
            else:
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        return count
    def range_query(self, low, high):
        if low > high:
            return []
        result, stack, node = [], [], self.root
        while stack or node is not None:
            while node is not None:
                if node.key >= low:
                    stack.append(node)
                    node = node.left
                else:
                    node = node.right  
            if not stack:
                break
            node = stack.pop()
            if node.key > high:
                break  
            result.append(node.key)
            node = node.right
        return result
    def is_valid_bst(self):
        if self.root is None:
            return True
        stack = [(self.root, None, None)]  
        while stack:
            node, lo, hi = stack.pop()
            if lo is not None and node.key <= lo:
                return False
            if hi is not None and node.key >= hi:
                return False
            if node.left is not None:
                stack.append((node.left, lo, node.key))
            if node.right is not None:
                stack.append((node.right, node.key, hi))
        return True