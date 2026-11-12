class graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_neighbors(self, node):
        return self.graph.get(node, [])
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
    def has_vertex(self, vertex):
        return vertex in self.graph
    def neighbors(self, vertex):
        return self.graph.get(vertex, [])
    def degree(self, vertex):
        return len(self.graph.get(vertex, []))
    def vertices(self):
        return list(self.graph.keys())
    def edges(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                if (v, u) not in edges:
                    edges.append((u, v))
        return edges
    def vertex_count(self):
        return len(self.graph)
    def edge_count(self):
        count = 0
        for u in self.graph:
            count += len(self.graph[u])
        return count // 2
    def __str__(self):
        return str(self.graph)