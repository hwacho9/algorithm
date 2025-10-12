N = list(map(int, input().split()))

# for i in range(len(N)):
#     for j in range(i, len(N)):
#         if N[i] > N[j]:
#             N[i], N[j] = N[j], N[i]

# for _ in N:
#     print(_, end=" ")


N.sort()
for i in N:
    print(i, end=" ")
