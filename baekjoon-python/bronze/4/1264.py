while True:
    A = input()
    count = 0
    if A == "#":
        break
    for i in A:
        if i in "aeiouAEIOU":
            count += 1

    print(count)
