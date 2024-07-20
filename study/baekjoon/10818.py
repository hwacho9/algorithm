from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
print(min(num), max(num))
