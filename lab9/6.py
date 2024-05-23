class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(graph_edges: list[tuple[int, int, int]], num_vertices: int) -> tuple[list[tuple[int, int, int]], int]:
    sorted_edges = sorted(graph_edges, key=lambda edge: edge[2])
    uf = UnionFind(num_vertices)

    mst = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight


def main():
    graph_edges = [
        (0, 1, 4),
        (0, 2, 4),
        (1, 2, 2),
        (1, 3, 6),
        (2, 3, 8),
        (2, 4, 9),
        (3, 4, 7),
    ]
    num_vertices = 5

    mst, total_weight = kruskal(graph_edges, num_vertices)
    print("Минимальное остовное дерево (ребра и их веса):")
    for u, v, weight in mst:
        print(f"({u}, {v}) - {weight}")
    print(f"Общий вес MST: {total_weight}\n ")

    graph_edges = [
        (0, 1, 6),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    num_vertices = 4

    mst, total_weight = kruskal(graph_edges, num_vertices)
    print("Минимальное остовное дерево (ребра и их веса):")
    for u, v, weight in mst:
        print(f"({u}, {v}) - {weight}")
    print(f"Общий вес MST: {total_weight}")


if __name__ == "__main__":
    main()
