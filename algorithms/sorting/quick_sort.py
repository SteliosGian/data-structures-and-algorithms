"""
Quick Sort Sorting Algorithm
"""


def quick_sort(arr: list, left: int, right: int) -> list:
    if left < right:
        pivot = right
        partition_index = partition(arr, pivot, left, right)

        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)
    return arr


def partition(arr: list, pivot: int, left: int, right: int) -> int:
    pivot_value = arr[pivot]
    partition_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, partition_index)
            partition_index += 1
    swap(arr, right, partition_index)
    return partition_index


def swap(arr: list, first_index: int, second_index: int) -> None:
    temp = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temp


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(arr, 0, len(arr) - 1))
