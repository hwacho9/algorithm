from sys import stdin


def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


n = int(stdin.readline())
print(fibonacci(n))
