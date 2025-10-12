A = int(input())
B = int(input())
C = int(input())

R = list(str(A * B * C))

for i in range(10):
    print(R.count(str(i)))
