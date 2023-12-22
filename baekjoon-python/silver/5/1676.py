import sys


def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


N = factorial(int(sys.stdin.readline()))
cnt = 0

for i in str(N)[::-1]:
    if i != "0":
        break
    cnt += 1

print(cnt)
