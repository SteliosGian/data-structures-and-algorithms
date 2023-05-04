"""
Bubble Sort Sorting Algorithm
"""


def bubble_sort(arr: list) -> list:
    length = len(arr)
    for i in range(length):
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                # Swap numbers
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(bubble_sort(arr))
