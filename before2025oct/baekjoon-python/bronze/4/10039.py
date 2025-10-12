A = []

for _ in range(5):
    A.append(int(input()))

sum = 0
for i in A:
    if i < 40:
        sum += 40
    else:
        sum += i

print(sum // 5)
