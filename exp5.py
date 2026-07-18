import random

comparison_count = 0


# ---------- Divide and Conquer ----------

def min_max_dc(arr, low, high):

    global comparison_count

    # One element
    if low == high:
        return arr[low], arr[low]

    # Two elements
    if high == low + 1:

        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    # Divide

    mid = (low + high) // 2

    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Combine

    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


# ---------- Naive Method ----------

def min_max_naive(arr):

    mn = arr[0]
    mx = arr[0]

    comps = 0

    for x in arr[1:]:

        comps += 1
        if x < mn:
            mn = x

        comps += 1
        if x > mx:
            mx = x

    return mn, mx, comps
# ---------- Demonstration ----------

arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

comparison_count = 0

mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comps = comparison_count

_, _, naive_comps = min_max_naive(arr)

print("Array :", arr)
print(f"\nMinimum Value : {mn}")
print(f"Maximum Value : {mx}")

# ---------- Added Features ----------

array_range = mx - mn
saved = naive_comps - dc_comps

print(f"Range of Array : {array_range}")

print(f"\nDivide & Conquer Comparisons : {dc_comps}")
print(f"Naive Comparisons            : {naive_comps}")
print(f"Comparisons Saved            : {saved}")

if naive_comps > 0:
    efficiency = (saved / naive_comps) * 100
    print(f"Efficiency Improvement       : {efficiency:.2f}%")

# ---------- Performance Analysis ----------

print(f'\n{"Size":>8} {"DC Comps":>12} {"Naive":>12} {"3n/2-2":>12}')
print("-" * 50)

for size in [10, 100, 1000, 10000]:

    arr = [random.randint(1, 10000) for _ in range(size)]

    comparison_count = 0

    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = 3 * size // 2 - 2

    print(f"{size:>8} {dc:>12} {naive:>12} {formula:>12}")

# ---------- Final Analysis ----------

print("\n========== Analysis ==========")

if dc_comps < naive_comps:
    print("Divide & Conquer uses fewer comparisons than the Naive method.")
elif dc_comps == naive_comps:
    print("Both methods use the same number of comparisons.")
else:
    print("Naive method performed better for this input.")

print("Program completed successfully.")