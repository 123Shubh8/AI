from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

    # The function to do BFS traversal.
    def bfs(self, v):
        visited = set()
        queue = deque([v])
        visited.add(v)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

if __name__ == "__main__":
    nodes = int(input("Enter the number of nodes: "))
    g = Graph()
    edges = int(input("Enter the number of edges: "))
    print("Enter the edges (u, v):")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    start_node = int(input("Enter the starting node for DFS & BFS: "))
    print("Following is Depth First Traversal (starting from vertex", start_node, "):")
    g.DFS(start_node)
    print("\nFollowing is Breadth First Traversal (starting from vertex", start_node, "):")
    g.bfs(start_node)