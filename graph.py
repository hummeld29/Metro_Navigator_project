from hash_table import HashTable
from linked_list import LinkedList

class edge:
    def __init__(self, to_vertex):
        self.to = to_vertex


class Graph:
    def __init__(self, directed=False):
        self.adj_list = HashTable()
        self.directed = directed

    def _check_vertex(self, name):
        if not isinstance(name, str):
            raise TypeError("vertex name must be a string")
        if name == "":
            raise ValueError("vertex name can't be a empty string")
    def add_vertex(self, name):
        self._check_vertex(name)
        if self.adj_list.contains(name):
            return False
        self.adj_list.put(name, LinkedList())
        return True
    def add_edge(self, from_vertex, to_vertex):
        self._check_vertex(from_vertex)
        self._check_vertex(to_vertex)
        if not self.adj_list.contains(from_vertex) or not self.adj_list.contains(to_vertex):
            raise KeyError("Both vertices must exist in the graph")
        if from_vertex == to_vertex:
            raise ValueError("Cannot add an edge from a vertex to itself")
        ulist = self.adj_list.get(from_vertex)
        curr = ulist.head
        while curr is not None:
            if curr.value.to == to_vertex:
                return False
            curr = curr.next
        ulist.append(edge(to_vertex))
        if not self.directed:
            to_list = self.adj_list.get(to_vertex)
            to_list.append(edge(from_vertex))
        return True
    def remove_edge(self, from_vertex, to_vertex):
        self._check_vertex(from_vertex)
        self._check_vertex(to_vertex)
        if not self.adj_list.contains(from_vertex) or not self.adj_list.contains(to_vertex):
            raise KeyError("Both vertices must exist in the graph")
        removed = False
        ulist = self.adj_list.get(from_vertex)
        curr = ulist.head
        index = 0
        while curr is not None:
            if curr.value.to == to_vertex:
                ulist.remove_at(index)
                removed = True
                break
            curr = curr.next
            index += 1
        if not self.directed:
            to_list = self.adj_list.get(to_vertex)
            curr = to_list.head
            index = 0
            while curr is not None:
                if curr.value.to == from_vertex:
                    to_list.remove_at(index)
                    break
                curr = curr.next
                index += 1
        return removed
    def remove_vertex(self, name):
        self._check_vertex(name)
        if not self.adj_list.contains(name):
            return False
        for key in self.adj_list.keys():
            if key == name:
               continue
            ulist = self.adj_list.get(key)
            curr = ulist.head
            index = 0
            while curr is not None:
                if curr.value.to == name:
                    ulist.remove_at(index)
                    break
                curr = curr.next
                index += 1
        self.adj_list.remove(name)
        return True
    def has_edge(self, from_vertex, to_vertex):
        self._check_vertex(from_vertex)
        self._check_vertex(to_vertex)
        if not self.adj_list.contains(from_vertex) or not self.adj_list.contains(to_vertex):
            return False
        curr = self.adj_list.get(from_vertex).head
        while curr is not None:
            if curr.value.to == to_vertex:
                return True
            curr = curr.next
        return False
    def has_vertex(self, name):
        self._check_vertex(name)
        return self.adj_list.contains(name)
    def neighbors(self, name):
        self._check_vertex(name)
        if not self.adj_list.contains(name):
            raise KeyError("Vertex does not exist in the graph")
        ulist = self.adj_list.get(name)
        neighbor_list = []
        curr = ulist.head
        while curr is not None:
            neighbor_list.append(curr.value.to)
            curr = curr.next
        return neighbor_list
    def degree(self, name):
        self._check_vertex(name)
        if not self.adj_list.contains(name):
            raise KeyError("Vertex does not exist in the graph")
        return len(self.neighbors(name))
    def __str__(self):
        line = ""
        for key in self.adj_list.keys():
            neighbors = ", ".join(self.neighbors(key))
            line += f"{key}: {neighbors}\n"
        return line
    def edge_count(self):
        count = 0
        for key in self.adj_list.keys():
            count += len(self.neighbors(key))
        if not self.directed:
            count //= 2
        return count
    def vertex_count(self):
        return len(self.adj_list.keys())
    def edges(self):
        edge_list = []
        for key in self.adj_list.keys():
            curr = self.adj_list.get(key).head
            while curr is not None:
                to = curr.value.to
                if self.directed or key < to:
                    edge_list.append((key, to))
                curr = curr.next
        return edge_list
        
            
    def vertices(self):
        return self.adj_list.keys()