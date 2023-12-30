import sys

N, M = map(int, sys.stdin.readline().split())
# numbers = [i for i in range(N, M + 1)]

# for num in range(N, M + 1):
#     non_prime = 0

#     if num > 1:
#         for i in range(2, int(num**0.5 + 1)):
#             if num % i == 0:
#                 non_prime += 1

#         if non_prime == 0:
#             print(num)


def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


for i in range(N, M + 1):
    if is_prime(i):
        print(i)
