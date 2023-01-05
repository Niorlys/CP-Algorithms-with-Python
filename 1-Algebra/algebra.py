from simple_timer import SimpleTimer
from to_compare import permute_test, fibonacci_dynamic2_test

"""
$-Binary Exponentiation
The goal is to compute a**n in O(log(n)), in order to achieve this, n is expressed in it's
binary representation, so computing a**n would be equivalent to compute int(log(n)) + 1 products. So it is left to
compute a**(2k) as faster as possible. It can be done by using the recursive relation:
a**n = (a**(n//2))**2 if not n % 2 else a(a**(n//2))**2 * a
"""


def binary_exponentiation_r(a, n):
    if n == 1:
        return a
    partial = binary_exponentiation_r(a, n // 2)
    return partial * partial if not n % 2 else partial * partial * a


def binary_exponentiation(a, n):
    r = 1
    while n:
        if n % 2:
            r = r * a
        a = a * a
        n = n // 2
    return r


"""
$-Applications
In practice the way of using binary exponentiation is by defining a map f: input_n |--> output_n,
then on the initial condition input_0, apply a composite operation of f n times: 
(f o f ... f o f)(input_0) = required_output, where f(input_n) have binary exponentiation
recursive relation..

1-Effective computation of x**n % m, where n could be a big number
It is easy to show that a * b ≡ (a%m * b%m) % m, so this is solved 
just replacing a by a%m and doing %m in each operation in the previous implementation.
Note the map here is f: x |--> (x * a)%m, and input_0 = a**0%m = 1 if m>1"""


def binary_exponentiation_l(a, n, m):
    a = a % m
    r = 1
    while n:
        if n % 2:
            r = r * a % m
        a = a * a % m
        n = n // 2
    return r


"""
2-Effective computation of Fibonacci numbers. 
The idea here comes from the recursive relation f_n = f_{n-1} + f_{n-2}. This gives us a hint about 
the transformation matrix that takes vector (f_i, f_{i+1}) to vector (f_{i+1}, f_{i+2}). Using as boundary 
conditions f_0 = 0, f_1 = 1, after solving the system (f_{i-2}, f_{i-1})A = (f_{i-1}, f_{i}), being 'A' a 
matrix of size 2x2, then we found out A =[[0, 1], [1, 1]]. Matrix recursive equation 
lead to (f_{0}, f_{1})A**(i-1) = (f_{i-1}, f_{i}), telling the ith Fibonacci number is the element [1][1] 
in the matrix A**(i-1), so raising the transformation matrix 'A' to n-1th power we  get the nth Fibonacci number. 
For computing the nth power we use same implementation applied to matrix. We use default to A 
for finding the nth Fibonacci number. Note the map here is f: X |-->  X * A
and input_0 = [[1, 0], [0, 1]]
"""


def fibonacci_matrix_l(n, m=10 ** 9 + 9, _A=[[0, 1], [1, 1]]):
    if n <= 1: return n
    _R = [[1, 0], [0, 1]]
    n -= 1

    def _AxB_2x2(__A, __B, md):  # multiply two 2x2 matrix
        row1 = [(__A[0][0] * __B[0][0] + __A[0][1] * __B[1][0]) % md,
                (__A[0][0] * __B[0][1] + __A[0][1] * __B[1][1]) % md]
        row2 = [(__A[1][0] * __B[0][0] + __A[1][1] * __B[1][0]) % md,
                (__A[1][0] * __B[0][1] + __A[1][1] * __B[1][1]) % md]
        return [row1, row2]

    while n:
        if n % 2:
            _R = _AxB_2x2(_R, _A, m)
        _A = _AxB_2x2(_A, _A, m)
        n = n // 2
    return _R[1][1]


"""
3- Applying a permutation n times

Given a sequence seq[0,1,2,...,n-1], and a permutation sequence p of the first n non negative integers, 
we need to perform f**n(seq), let say applying f composite with itself n times, where f: seq[σ_n]|-->seq[p],
input_0 = given_seq
"""


def permute(r, p, n):
    def apply_permutation(arr, perm):
        return [arr[value] for value in perm]
    while n:
        if n % 2:
            r = apply_permutation(r, p)
        p = apply_permutation(p, p)
        n = n // 2
    return r


if __name__ == '__main__':
    # Testcases evidencing differences
    #st = SimpleTimer(((774901, 877549,10**9+9),), lambda a,n,m:a**n%m, binary_exponentiation_l)
    #st = SimpleTimer((1000000,), fibonacci_dynamic2_test, fibonacci_matrix_l)
    #st = SimpleTimer((([1,2,3,4,5], [4,3,2,1,0], 1000000),), permute, permute_test)
    #st()
    pass
