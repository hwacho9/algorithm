n = int(input())  # 분해합을 입력값으로 받음

for i in range(n):  # 해당 분해합의 생성자 찾기
    # print(i)
    digit_sum = i + sum(map(int, str(i)))
    if digit_sum == n:
        print(i)
        break
else:
    print(0)
