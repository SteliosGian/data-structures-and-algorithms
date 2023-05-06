"""
Fibonacci with Dynamic Programming

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
"""


# Time complexity - O(2^n)
# Space complexity - O(1)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


cache = {}


# Time complexity - O(n)
# Space complexity - O(n)
def fibonacci_faster(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = fibonacci_faster(n-1) + fibonacci_faster(n-2)
            return cache[n]


def fibonacci_faster2(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-2] + answer[i-1])
    return answer.pop()


print(fibonacci(7))
print(fibonacci_faster(7))
print(fibonacci_faster2(7))
