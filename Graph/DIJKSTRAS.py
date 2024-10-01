#Dijkstra's Algorithm finds the shortest paths from a
#single source node to all other nodes in a weighted 
#graph with non-negative edge weights.
#0. Import Heapq
import heapq

#1. Create class which creates graph

class Graph:
    def __init__(self):
        self.adjacency_ls = {}

    def add_node(self, node):
        if node not in self.adjacency_ls:
            self.adjacency_ls[node] = []

    def add_edge(self, prev_node, foll_node, weight=1, directed=False):
        self.add_node(prev_node)
        self.add_node(foll_node)
        self.adjacency_ls[prev_node].append((foll_node, weight))
        if not directed:
            self.adjacency_ls[foll_node].append((prev_node, weight))

    def get_neighbors(self, node):
        return self.adjacency_ls.get(node, [])

    def __str__(self):
        return '\n' + '\n'.join(f"{node}: {neighbors}" for node, neighbors in self.adjacency_ls.items())

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph.adjacency_ls}   
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)

        if curr_distance > distances[curr_node]:
            continue

        for neighbor, weight in graph.get_neighbors(curr_node):
            distance = curr_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# Create a graph instance
graph = Graph()

# Add edges (nodes will be added automatically)
graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'D', 1)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 2)
graph.add_edge('C', 'E', 3)
graph.add_edge('D', 'E', 1)

# Display the graph
print(graph)

shortest_distances = dijkstra(graph, 'A')

print("Shortest distances from node 'A':")
for node, distance in shortest_distances.items():
    print(f"Distance to {node}: {distance}")
