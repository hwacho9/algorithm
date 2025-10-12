from sys import stdin

a, b = map(int, stdin.readline().split())
array = [0]
sum = 0

for i in range(b + 1):
    for j in range(i):
        array.append(i)


for i in range(a, b + 1):
    sum += array[i]

print(sum)
