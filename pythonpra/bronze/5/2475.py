# A, B, C, D, E = map(int, input().split())
num = list(map(int, input().split()))
# print(num)

result = 0

for i in num:
    result += i**2

print(result % 10)
