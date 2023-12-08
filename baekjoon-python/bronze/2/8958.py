A = int(input())


for i in range(A):
    test = input()
    score = 0
    sumScore = 0
    for i in test:
        if i == "O":
            score += 1
            sumScore += score
        else:
            score = 0
    print(sumScore)
