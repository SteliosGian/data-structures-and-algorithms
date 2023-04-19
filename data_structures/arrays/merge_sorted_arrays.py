"""
Given two sorted arrays, merge the arrays into a one sorted array
[0, 3, 4, 31] and [4, 6, 30] should return [0, 3, 4, 4, 6, 30, 31]
"""


# O(n)
def merge_sorted_arrays(array1: list, array2: list) -> list:
    merged_array = []
    i = 0
    j = 0

    # Check input
    if not array1:
        return array2
    if not array2:
        return array1

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        elif array2[j] < array1[i]:
            merged_array.append(array_2[j])
            j += 1

    return merged_array + array1[i:] + array2[j:]


array_1 = [0, 3, 4, 31]
array_2 = [4, 6, 30]

print(merge_sorted_arrays(array_1, array_2))
