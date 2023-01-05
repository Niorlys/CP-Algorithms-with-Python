from sys import stdin as std
# Problem 1: https://codeforces.com/problemset/problem/630/I
# Solution: It is easy to show the required number for n is 4**(n-3)(9n-3). To see this, consider three cases:
# 1- the n cars of the same make are parked at the start, here there are 4*3*4**(n-3) ways
# 2- the n cars of the same make are parked at the middle, here there are 4*(n-3)*3**2*4**(n-4)
# 3- the n cars of the same make are parked at the end, here there are 4*3*4**(n-3) ways
# adding three expressions above we get 4**(n-3)(9n-3)
def bin_exp(a, n):
    r = 1
    while n:
        if n % 2:
            r = r * a
        a = a * a
        n = n // 2
    return r


solution = lambda n: bin_exp(4, n - 3) * (9 * n - 3)
print(solution(int(std.readline())))


# Problem 2: https://www.spoj.com/problems/LASTDIG/
# Solutions: We need to compute a**b%10. At first, using that a**b%10 ≡ (a%10)**b % 10, we use just modular binary
# exponentiation, and that's it!
# A second (and better) solution is computing all possibles k<10 last digits of the powers of a, let say they are stored
# in list d, then return d[b%len(d) - 1]

def modular_bin_exp(a, n, m=10):
    a = a % m
    r = 1
    while n:
        if n % 2:
            r = r * a % m
        a = a * a % m
        n = n // 2
    return r


t = int(std.readline())
while t:
    print(modular_bin_exp(*map(int, std.readline().split())))
    t = t - 1

# Code for solution 2:
def sol2(a,b):
    am = a % 10
    d = [am]
    pm = (a * a) % 10
    while pm != am:
        d.append(pm)
        pm = (pm * a) % 10
    return d[b%len(d)-1] # This returns last digit of a**b

# Problem 3: https://www.spoj.com/problems/ZSUM/
# Solution: Just use binary exponentiation in a regular flat way

def modular_bin_exp(a, n, m=10000007):
    a = a % m
    r = 1
    while n:
        if n % 2:
            r = r * a % m
        a = a * a % m
        n = n // 2
    return r


def z(n,k):
    return (modular_bin_exp(n,n) + modular_bin_exp(n,k) + 2*modular_bin_exp(n-1,n-1)
            + 2*modular_bin_exp(n-1,k))%10000007

t = std.readline()
while t != '0 0':
    print(z(*map(int, t.split())))
    t = std.readline()


# Problem 4: https://www.codechef.com/JAN221B/problems/RIFFLES
# Solutions is easy applying a permutations operation K times, using binary exponentiation.
def exp_permutation(seq,p, n):
    def permute(_seq, permutation):
        return [_seq[i] for i in permutation]
    while n:
        if n % 2:
            seq = permute(seq, p)
        p = permute(p, p)
        n = n // 2
    return seq

t = int(std.readline())
while t:
    N, K = map(int, std.readline().split())
    seq = list(range(1, N + 1))
    p = [i - 1 for i in range(1, N, 2)] + [i - 1 for i in range(2, N + 1, 2)]
    for k in exp_permutation(seq, p , K):
        print(k, end=' ')
    print()
    t = t - 1

