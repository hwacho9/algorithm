A = []

for _ in range(3):
    A.append(int(input()))

temp = list(set(A))

if len(temp) == 1 and temp[0] == 60:
    print("Equilateral")
elif len(temp) == 2 and sum(A) == 180:
    print("Isosceles")
elif len(temp) == 3 and sum(A) == 180:
    print("Scalene")
else:
    print("Error")
