"""
Insertion Sort Sorting Algorithm
"""


def insertion_sort(arr: list) -> list:
    i = 1
    end = arr[0]
    while i < len(arr):
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end = arr[i]
        i += 1
    return arr


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(insertion_sort(arr))
