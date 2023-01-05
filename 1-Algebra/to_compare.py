"""This module is just a functions storage to compare performance"""


# Recursive: very slow, and it is better to avoid this implementation
def fibonacci_test(n: int) -> int:
    if n <= 1: return n
    return fibonacci_test(n - 1) + fibonacci_test(n - 2)


def fibonacci_dynamic2_test(n):
    if n<= 1: return n
    x, y = 0, 1
    for _ in range(n - 1):
        x, y = y, (x + y)%(10**9+9)
    return y

def permute_test(seq, p, n):
    for _ in range(n):
        seq = [seq[value] for value in p]
    return seq
