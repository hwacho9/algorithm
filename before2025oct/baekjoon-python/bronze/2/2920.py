A = input().split()


ascend = sorted(A)
descend = sorted(A, reverse=True)

if A == ascend:
    print("ascending")
elif A == descend:
    print("descending")
else:
    print("mixed")
