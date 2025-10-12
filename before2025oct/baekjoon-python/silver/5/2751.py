import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    A.append(int(sys.stdin.readline()))

A.sort()
for i in A:
    print(i)
