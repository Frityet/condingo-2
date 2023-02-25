"""
This function takes in an integer, x, and returns x / 2 if
x is even and 3x + 1 if x is odd.

Arguments:
    num (Int): An integer
Returns:
    x / 2 if x is even and 3x + 1 if x is odd.
Examples:
    10 => 5
    3 => 10
"""

def number_transform(x):
    """
    Write your function here!
    """
    return x / 2 if x % 2 == 0 else x * 3 + 1
    pass
