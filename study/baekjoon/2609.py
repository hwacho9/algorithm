# ユークリッドの互除法

from sys import stdin


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


a, b = map(int, stdin.readline().split())
print(gcd(a, b))
print(lcm(a, b))
