"""
Create a function that reverses a string:
"Hi my name is Stelios" should be
"soiletS si eman ym iH"
"""


# O(n)
def reverse(input: str) -> str:
    # Check input
    if not isinstance(input, str) or (len(input) < 2):
        return "Not a valid string"
    # Reverse string
    reversed_string = ''.join([s for s in input[::-1]])
    return reversed_string


test_case = "Hi my name is Stelios"

print(reverse(test_case))

print(reverse(1))
