def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


N, K = map(int, input().split())

# print(factorial(N))
ans = factorial(N) / (factorial(N - K) * factorial(K))

print(int(ans))
