from hash_table import HashTable
from linked_list import LinkedList

class edge:
    def __init__(self, to_vertex):
        self.to = to_vertex


class Graph:
    def __init__(self, directed=False):
        self.hash_table = HashTable()
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
            raise ValueError("Both vertices must exist in the graph")
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
            raise ValueError("Both vertices must exist in the graph")
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
        ulist = self.adj_list.get(name)
        curr = ulist.head
        while curr is not None:
            to_vertex = curr.value.to
            to_list = self.adj_list.get(to_vertex)
            index = 0
            temp = to_list.head
            while temp is not None:
                if temp.value.to == name:
                    to_list.remove_at(index)
                    break
                temp = temp.next
                index += 1
            curr = curr.next
        self.adj_list.remove(name)
        return True