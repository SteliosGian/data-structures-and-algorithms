"""
Write two functions that find the factorial of any number.
One should use recursion, the other should just use a for loop.
"""


# O(n)
def find_factorial_recursive(number: int) -> int:
    if number == 2:
        return number
    elif number == 1:
        return number

    return number * find_factorial_recursive(number-1)


# O(n)
def find_factorial_iterative(number: int) -> int:
    res = 1
    for num in range(1, number+1):
        res *= num
    return res


print(find_factorial_recursive(5))  # Should return 120

print(find_factorial_iterative(5))  # Should return 120
