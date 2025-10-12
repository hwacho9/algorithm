while True:
    N = list(input())

    A = list(reversed(N))

    if N == ["0"]:
        break

    cnt = 0
    for i in range(len(N)):
        if N[i] == A[i]:
            cnt += 1
        else:
            cnt -= 1

    if cnt == len(N):
        print("yes")
    else:
        print("no")


"""n = input()

while True:
if n == '0':
	break
else:
  if n == n[::-1]:  슬라이싱
      print("yes")
  else:
      print("no")

"""
