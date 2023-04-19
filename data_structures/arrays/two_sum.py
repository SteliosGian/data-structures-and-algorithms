"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""


# O(n^2)
def two_sum(nums: list, target: int) -> list:
    # Check input
    if not nums:
        return nums

    for index1 in range(len(nums)):
        for index2 in range(1, len(nums)):
            if index1 == index2:
                continue
            elif nums[index1] + nums[index2] == target:
                return [index1, index2]


# O(n)
def two_sum_faster(nums: list, target: int) -> list:
    # Check input
    if not nums:
        return nums

    d = {}
    for index, num in enumerate(nums):
        m = target - num
        if m in d:
            return [d[m], index]
        else:
            d[num] = index


array = [2, 7, 11, 15]
target = 9

print(two_sum(array, target))
print(two_sum_faster(array, target))
