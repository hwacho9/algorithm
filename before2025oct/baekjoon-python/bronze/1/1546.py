N = int(input())
A = list(map(int, input().split()))
B = []

M = max(A)

for i in range(len(A)):
    B.append(A[i] / M * 100)

# print(B)

print(sum(B) / N)
