def selection_sort(arr):
    n = len(arr)

    for i in range(n):
    
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

       
        arr[i], arr[min_index] = arr[min_index], arr[i]

print("\nFor Selection Sort\n")
user_input = input("Enter the array elements separated by spaces: ")
arr = [int(x) for x in user_input.split()]

print("Original array:", arr)


selection_sort(arr)

print("Sorted array:", arr)


#Prims Algorithm

import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        visited = [False] * self.vertices
        min_heap = [(0, 0)]  # (weight, vertex)
        mst_weight = 0

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if not visited[u]:
                mst_weight += weight
                visited[u] = True

                for v, w in self.graph[u]:
                    if not visited[v]:
                        heapq.heappush(min_heap, (w, v))

        return mst_weight

# Get user input for the number of vertices and edges
print("\nFor Prims Algorithm\n")
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Create the graph
g = Graph(num_vertices)

# Get user input for each edge
for _ in range(num_edges):
    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
    g.add_edge(u, v, weight)

# Calculate and print the weight of the minimum spanning tree
minimum_spanning_tree_weight = g.prim_mst()
print("Weight of Minimum Spanning Tree:", minimum_spanning_tree_weight)

