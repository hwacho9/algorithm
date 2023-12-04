H, M, S = map(int, input().split())
T = int(input())

S = S + T
M += S // 60
H += M // 60

M = M % 60
S = S % 60
H = H % 24
print(H, M, S)
