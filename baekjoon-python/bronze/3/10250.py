N = int(input())

for i in range(N):
    H, W, N = map(int, input().split())
    Y = N % H
    X = (N // H) + 1
    if Y == 0:
        Y = H
        X -= 1

    print(f"{Y* 100 + X}")
