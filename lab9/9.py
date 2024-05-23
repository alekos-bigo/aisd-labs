import heapq


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.adjacency_list:
            self.adjacency_list[vertex_id] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            self.adjacency_list[from_vertex].append((to_vertex, weight))

    def dijkstra(self, start, end):
        distances = {vertex: float("infinity") for vertex in self.adjacency_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            if current_vertex == end:
                break

            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances[end] if distances[end] != float("infinity") else None

    def __str__(self):
        return str(self.adjacency_list)


def main():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)

    start_vertex = "A"
    end_vertex = "D"
    shortest_path_distance = graph.dijkstra(start_vertex, end_vertex)
    print(f"Граф: {graph}")
    print(f"Кратчайшее расстояние от {start_vertex} до {end_vertex}: {shortest_path_distance}\n")

    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "D", 1)
    graph.add_edge("A", "C", 6)
    graph.add_edge("B", "E", 8)
    graph.add_edge("D", "E", 12)
    graph.add_edge("D", "C", 4)
    graph.add_edge("C", "E", 4)

    start_vertex = "A"
    end_vertex = "E"
    shortest_path_distance = graph.dijkstra(start_vertex, end_vertex)
    print(f"Граф: {graph}")
    print(f"Кратчайшее расстояние от {start_vertex} до {end_vertex}: {shortest_path_distance}")


if __name__ == "__main__":
    main()
