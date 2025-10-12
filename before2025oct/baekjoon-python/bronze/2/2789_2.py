from itertools import combinations


N, M = map(int, input().split())
card = list(map(int, input().split()))

ans = 0

for i in combinations(card, 3):
    if ans < sum(i) <= M:
        ans = sum(i)

print(ans)
