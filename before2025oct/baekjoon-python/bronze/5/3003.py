# 1 1 2 2 2 8
chess = [1, 1, 2, 2, 2, 8]
num = list(map(int, input().split()))

result = []

for i in range(len(num)):
    result.append(chess[i] - num[i])

for i in result:
    print(i, end=" ")
