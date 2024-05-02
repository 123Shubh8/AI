class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start_vertex):
        visited = set()
        self.dfs_recursive(start_vertex, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)

g = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    edge = input("Enter edge (format: u v): ").split()
    u, v = map(int, edge)
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex for traversal: "))

print("\nDepth First Search (DFS):")
g.dfs(start_vertex)

print("\nBreadth First Search (BFS):")
g.bfs(start_vertex)
