'''
Given an array, return the first recurring character.
array = [2,5,1,2,3,5,1,2,4]
should return 2
array = [2,1,1,2,3,5,1,2,4]
should return 1
array = [2,3,4,5]
should return None
'''
from typing import Optional


# Time complexity - O(n^2)
# Space complexity - O(1)
def first_recurring_character_slow(input: list) -> Optional[int]:

    # Input check
    if not input:
        return None

    length = len(input)
    i = 0
    res = None
    while i < length:
        j = i+1
        while j < length:
            if input[i] == input[j]:
                length = j
                res = input[j]
                continue
            else:
                j += 1
        i += 1
    return res


# Time complexity - O(n)
# Space complexity - O(n)
def first_recurring_character(input: list) -> Optional[int]:
    occurrences = {}

    # Input check
    if not input:
        return None

    for i in input:
        if i in occurrences:
            return i
        else:
            occurrences[i] = 1
    return None


array_1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]  # Should return 2
array_2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]  # Should return 1
array_3 = [2, 3, 4, 5]  # Should return None

print(first_recurring_character_slow(array_1))
print(first_recurring_character_slow(array_2))
print(first_recurring_character_slow(array_3))

print(first_recurring_character(array_1))
print(first_recurring_character(array_2))
print(first_recurring_character(array_3))
