"""
Implement a function that reverses a string using iteration and recursion.
"""


def reverse_string_iterative(x: str) -> str:
    res = []
    for i in x[::-1]:
        res.append(i)
    return ''.join(res)


def reverse_string_recursive(x: str) -> str:
    if len(x) == 0:
        return ""

    return reverse_string_recursive(x[1:]) + x[0]


x = "hello my name is stelios"

print(reverse_string_iterative(x))  # Should return "soilets si eman ym olleh"


print(reverse_string_recursive(x))  # # Should return "soilets si eman ym olleh"
