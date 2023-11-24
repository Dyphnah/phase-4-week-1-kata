
def unsorted_subarray(arr):
    n = len(arr)

    m = 0

    while m < n - 1 and arr[m] <= arr[m + 1]:
        m += 1

    if m == n - 1:
        return [0, 0]

    n = n - 1
    while n > 0 and arr[n] >= arr[n - 1]:
        n -= 1

    min_val = min(arr[m:n + 1])
    max_val = max(arr[m:n + 1])

    while m > 0 and arr[m - 1] > min_val:
        m -= 1

    while n < len(arr) - 1 and arr[n + 1] < max_val:
        n += 1

    return [m, n]


arr = [1, 2, 3, 6, 4, 4, 5, 7]
result = unsorted_subarray(arr)
print(result)


# Part 2 of the Kata

def sorted_array(arr):
    return sorted(arr, key=len)

arr = ["Telescopes", "Glasses", "Eyes", "Monocles"]
sorted_arr =sorted_array(arr)
print(sorted_arr)