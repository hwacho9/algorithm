import sys

N = int(sys.stdin.readline())

point = []

for i in range(N):
    point.append(list(map(int, sys.stdin.readline().split())))

point.sort()

for i in point:
    print(i[0], i[1])
