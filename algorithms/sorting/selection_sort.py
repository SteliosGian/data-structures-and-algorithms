"""
Selection Sort Sorting Algorithm
"""


def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        min = i
        temp = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                # Update minimum if current is lower
                # that what we had previously
                min = j
        arr[i] = arr[min]
        arr[min] = temp
    return arr


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(selection_sort(arr))
