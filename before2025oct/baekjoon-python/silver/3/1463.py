import sys

N = int(sys.stdin.readline())
n = 0

while N != 1:
    if N % 3 == 0:
        N = N / 3
        n += 1
        print(N)
    elif N % 2 == 0:
        N = N / 2
        n += 1
        print(N)
    else:
        N -= 1
        n += 1
        print(N)

print(n)
