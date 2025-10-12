A = []

for i in range(5):
    A.append(int(input()))

H = A[:3]
V = A[-2:]

print(min(H) + min(V) - 50)
