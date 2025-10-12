N = int(input())
A = input()

alp = "abcdefghijklmnopqrstuvwxyz"


sum = 0
for i in range(N):
    sum += (ord(A[i]) - 96) * pow(31, i)

print(sum)
