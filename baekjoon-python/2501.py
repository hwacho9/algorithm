from sys import stdin

N, K = map(int, stdin.readline().split())
divisor = []

for i in range(1, N + 1):
    if int(N) % i == 0:
        divisor.append(i)

if len(divisor) >= K:
    print(divisor[K - 1])
else:
    print(0)
