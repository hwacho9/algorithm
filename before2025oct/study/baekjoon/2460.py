from sys import stdin

sum = 0
result = []

for _ in range(10):
    getOn, getOff = map(int, stdin.readline().split())
    now = getOff - getOn
    sum += now
    result.append(sum)

print(max(result))

# https://www.acmicpc.net/problem/2460
