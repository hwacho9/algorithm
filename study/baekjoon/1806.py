from sys import stdin

N, S = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))

left = 0
right = 0
length = 100000
sum = array[0]


while left <= right:
    if sum >= S:
        length = min(length, right - left + 1)
        sum -= array[left]
        left += 1
    else:
        right += 1
        if right < N:
            sum += array[right]
        else:
            break

if length == 100000:
    print(0)
else:
    print(length)
