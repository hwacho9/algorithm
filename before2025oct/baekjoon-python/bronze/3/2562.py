N = []

for i in range(9):
    N.append(int(input()))

print(max(N))
number = 0
for i in N:
    number = number + 1
    if max(N) == i:
        print(number)
