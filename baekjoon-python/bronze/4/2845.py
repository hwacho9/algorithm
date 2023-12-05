L, P = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    print(i - L * P, end=" ")
