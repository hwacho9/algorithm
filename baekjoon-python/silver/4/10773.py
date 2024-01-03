from collections import deque
import sys

N = int(sys.stdin.readline())
deq = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        deq.pop()
    else:
        deq.append(num)

if len(deq) == 0:
    print(0)
else:
    print(sum(deq))
