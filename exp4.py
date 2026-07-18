import heapq

# ---------- Dijkstra Algorithm ----------

def dijkstra(graph, source):

    n = len(graph)

    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]
    visited = set()

    while pq:

        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:

            if dist[u] + w < dist[v]:

                dist[v] = dist[u] + w
                prev[v] = u

                heapq.heappush(pq, (dist[v], v))

    return dist, prev


# ---------- Path Reconstruction ----------

def reconstruct_path(prev, source, target):

    path = []

    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []
# ---------- Graph Definition ----------

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

source = 0

dist, prev = dijkstra(graph, source)

print(f"\nShortest paths from vertex {source}\n")

print(f'{"Vertex":>8} {"Distance":>10} {"Path":>25}')
print("-" * 50)

reachable = 0
nearest_vertex = source
nearest_distance = float("inf")
farthest_vertex = source
farthest_distance = 0

for v in range(len(graph)):

    path = reconstruct_path(prev, source, v)

    if path:
        path_str = " -> ".join(map(str, path))
    else:
        path_str = "No Path"

    if dist[v] != float("inf"):
        d = dist[v]
        reachable += 1

        if v != source:
            if d < nearest_distance:
                nearest_distance = d
                nearest_vertex = v

            if d > farthest_distance:
                farthest_distance = d
                farthest_vertex = v
    else:
        d = "INF"

    print(f"{v:>8} {str(d):>10} {path_str:>25}")

# ---------- Additional Analysis ----------

print("\n========== Analysis ==========")

print(f"Reachable Vertices : {reachable}")

print(f"Nearest Vertex : {nearest_vertex} (Distance = {nearest_distance})")

print(f"Farthest Vertex : {farthest_vertex} (Distance = {farthest_distance})")

print("\nDijkstra's algorithm successfully computed the shortest paths from the source vertex.")