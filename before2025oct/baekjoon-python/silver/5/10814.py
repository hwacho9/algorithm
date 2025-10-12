import sys

N = int(sys.stdin.readline())

user = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    user.append([int(age), name])

user.sort(key=lambda x: x[0])

for i in user:
    print(i[0], i[1])
