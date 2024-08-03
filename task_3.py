import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges):
        self.vertices[vertex] = edges

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example usage:
graph = Graph()
graph.add_vertex('A', {'B': 1, 'C': 4})
graph.add_vertex('B', {'A': 1, 'C': 2, 'D': 5})
graph.add_vertex('C', {'A': 4, 'B': 2, 'D': 1})
graph.add_vertex('D', {'B': 5, 'C': 1})

distances = graph.dijkstra('A')

for vertex, distance in distances.items():
    print(f"Distance from A to {vertex} is {distance}")