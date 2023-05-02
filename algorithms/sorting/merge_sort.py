"""
Merge Sort Sorting Algorithm
"""
import math


def merge_sort(arr: list) -> list:
    length = len(arr)
    if length == 1:
        return arr
    # Split array in into right and left
    middle = math.floor(length / 2)
    left = arr[0:middle]
    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list) -> list:
    result = []
    left_index = 0
    right_index = 0
    while (left_index < len(left)) and (right_index < len(right)):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + left[left_index:] + right[right_index:]


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(arr))
