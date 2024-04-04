"""Recursive_fibonacci"""


def recursive_fibonacci(n):
    """Recursive_fibonacci"""
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


print(recursive_fibonacci(10))
