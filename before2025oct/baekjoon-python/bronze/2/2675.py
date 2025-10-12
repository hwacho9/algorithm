S = int(input())

for i in range(S):
    R, P = input().split()

    for i in P:
        print(i * int(R), end="")
    print()
