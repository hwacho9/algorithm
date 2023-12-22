import sys

A = []
N = int(sys.stdin.readline())

for i in range(N):
    A.append(input())

lst = list(set(A))
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)
