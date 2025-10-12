students = []

for i in range(1, 31):
    students.append(i)

kadai = []

for i in range(28):
    kadai = int(input())
    students.remove(kadai)

print(min(students))
print(max(students))
