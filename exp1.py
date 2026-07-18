import time
import random

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + int(((target - arr[low]) * (high - low)) /
                        (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():

    sizes = [1000, 5000, 10000, 50000, 100000]

    print(f"\n{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} {'IS Comp':>12} {'BS Comp':>12}")
    print("-" * 70)

    for size in sizes:

        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} {comp_is:>12} {comp_bs:>12}")

        # ---- Added Analysis ----
        if is_time < bs_time:
            print("   Faster Algorithm : Interpolation Search")
        elif bs_time < is_time:
            print("   Faster Algorithm : Binary Search")
        else:
            print("   Both algorithms took nearly the same time.")

        print(f"   Time Difference  : {abs(is_time-bs_time):.4f} ms\n")


# ---------------- MAIN ---------------- #

arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

idx1, comp1 = interpolation_search(arr, target)
idx2, comp2 = binary_search(arr, target)

print("Array :", arr)
print("Target :", target)

print("\nInterpolation Search")
print(f"Index Found : {idx1}")
print(f"Comparisons : {comp1}")

print("\nBinary Search")
print(f"Index Found : {idx2}")
print(f"Comparisons : {comp2}")

# ---- Added Verification ----
if idx1 == idx2:
    print("\nResult Verification : Both algorithms returned the same index.")
else:
    print("\nResult Verification : Outputs are different.")

performance_analysis()