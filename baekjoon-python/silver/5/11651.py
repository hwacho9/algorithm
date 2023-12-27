import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    num.append(list(map(int, sys.stdin.readline().split())))

num.sort(key=lambda x: (x[1], x[0]))
""" 두번째 값을 기준으로 오름차순 
두 번째 값이 같을때는 첫번째 값을 기준으로 오름차순
내림차순일때는 -x[1]
"""
for i in num:
    print(i[0], i[1])
