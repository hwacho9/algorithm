# 브루트포스 알고리즘
# 완전 탐색

from sys import stdin
import itertools

all = [int(stdin.readline()) for _ in range(9)]

for i in itertools.combinations(all, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
