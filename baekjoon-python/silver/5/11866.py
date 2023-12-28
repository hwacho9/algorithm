import sys

N, K = map(int, sys.stdin.readline().split())

queue = [i for i in range(1, N + 1)]
result = []
index = 0
# print(f"a{len(queue)}")

while len(queue) != 0:
    index += K - 1
    index = index % len(queue)
    # print(index, len(queue))
    result.append(str(queue.pop(index)))

print("<", ", ".join(result), ">", sep="")

# A = [1, 2, 3, 4, 5, 6, 7]
# print(A[2])
# print(A.pop(2))
# print(A)
# print(A[2])
# # print(A[2])
