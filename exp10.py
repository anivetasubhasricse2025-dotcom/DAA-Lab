import random
import time
import sys

sys.setrecursionlimit(20000)

comparisons = 0


def partition(arr, low, high):

    global comparisons

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        comparisons += 1

        if arr[j] <= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def deterministic_quicksort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


def randomized_quicksort(arr, low, high):

    if low < high:

        rand_idx = random.randint(low, high)

        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        pi = partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


def run_test(name, sort_fn, arr):

    global comparisons

    a = arr[:]

    comparisons = 0

    start = time.perf_counter()

    sort_fn(a, 0, len(a) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


N = 5000

test_cases = {

    "Random": [random.randint(1, 100000) for _ in range(N)],

    "Sorted": list(range(N)),

    "Reverse": list(range(N, 0, -1)),

    "Nearly Sorted": list(range(N))

}

ns = test_cases["Nearly Sorted"]

for _ in range(N // 20):

    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)

    ns[i], ns[j] = ns[j], ns[i]

print("========== Quick Sort Performance Analysis ==========\n")

print(f"Input Size : {N}\n")

print(f'{"Input Type":<16} {"DQS Comps":>12} {"DQS Time(ms)":>14} {"RQS Comps":>12} {"RQS Time(ms)":>14}')

print("-" * 72)
print("-" * 72)

for case, arr in test_cases.items():

    d_comps, d_time = run_test("DQS", deterministic_quicksort, arr)

    r_comps, r_time = run_test("RQS", randomized_quicksort, arr)

    print(f"{case:<16} {d_comps:>12} {d_time:>14.2f} {r_comps:>12} {r_time:>14.2f}")

# ---------------- Summary ----------------

print("\n========== Analysis ==========\n")

print(f"Number of Test Cases : {len(test_cases)}")

print(f"Input Size           : {N}")

print("\nObservation:")

print("Deterministic Quick Sort always selects the last element")
print("as the pivot. It performs efficiently for random data")
print("but may perform poorly on already sorted or reverse")
print("sorted inputs because of unbalanced partitions.\n")

print("Randomized Quick Sort selects a random pivot before")
print("partitioning. This reduces the chance of worst-case")
print("performance and usually provides better average")
print("execution time for different input patterns.\n")

print("Conclusion:")

print("Randomized Quick Sort is generally preferred in practice")
print("because random pivot selection minimizes the probability")
print("of worst-case O(n²) behavior while maintaining an average")
print("time complexity of O(n log n).")

print("\nProgram executed successfully.")