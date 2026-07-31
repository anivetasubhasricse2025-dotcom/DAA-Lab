import heapq
from itertools import permutations

INF = float('inf')


def reduce_matrix(mat):
    """Reduce matrix and return reduction cost"""

    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min and row_min != INF:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min and col_min != INF:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_brute_force(cost, n):
    """Brute Force TSP"""

    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    for perm in permutations(cities):

        path = [0] + list(perm) + [0]

        current_cost = sum(cost[path[i]][path[i + 1]] for i in range(n))

        if current_cost < best_cost:
            best_cost = current_cost
            best_path = path

    return best_path, best_cost


# ---------------- Main Program ----------------

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

n = 5

cities = ['A', 'B', 'C', 'D', 'E']

best_path, best_cost = tsp_brute_force(cost, n)

print("========== Travelling Salesman Problem ==========\n")

print("Cost Matrix:\n")

print(f'{"":>4}', ' '.join(f'{c:>5}' for c in cities))

for i, row in enumerate(cost):

    values = ["INF" if x == INF else str(x) for x in row]

    print(f'{cities[i]:>4}', ' '.join(f'{v:>5}' for v in values))
print("\nOptimal Tour : ", " -> ".join(cities[i] for i in best_path))

print(f"Minimum Cost : {best_cost}")

print("\nPath Verification:")

for i in range(n):

    u = best_path[i]
    v = best_path[i + 1]

    print(f"{cities[u]} -> {cities[v]} : Cost = {cost[u][v]}")

# ---------- Additional Details ----------

print("\n========== Analysis ==========")

print(f"Number of Cities   : {n}")

print(f"Starting City      : {cities[best_path[0]]}")

print(f"Ending City        : {cities[best_path[-1]]}")

print(f"Total Edges Travelled : {len(best_path) - 1}")

print(f"Optimal Tour Cost  : {best_cost}")

print("\nObservation:")

print("Brute Force checks every possible tour.")

print("The minimum cost among all possible tours is selected.")

print("This method guarantees the optimal solution but")

print("its time complexity increases rapidly as the number")

print("of cities increases.")

print("\nProgram executed successfully.")