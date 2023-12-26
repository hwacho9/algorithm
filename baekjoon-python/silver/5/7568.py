import sys

N = int(sys.stdin.readline())

A = []
ans = []
for i in range(N):
    A.append(list(map(int, input().split())))

# print(A)

for i in range(N):
    count = 1
    for j in range(N):
        if A[i][0] < A[j][0] and A[i][1] < A[j][1]:
            count += 1
    ans.append(count)

for i in ans:
    print(i, end=" ")
