# stack
# LIFO
# stack initilation stack = []

# stack = [1,2,3]
# stack.append(4) --> [1,2,3,4]

# stack - pop
# top = stack.pop -> 4 & stack -> [1,2,3]

# stack[-1] -> 4 , stack = [1,2,3,4]

from sys import stdin

input = list(stdin.readline())

stack = []
tmp = 1
ans = 0

for i in range(len(input)):

    if input[i] == "(":
        stack.append(input[i])
        tmp *= 2

    elif input[i] == "[":
        stack.append(input[i])
        tmp *= 3

    elif input[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if input[i - 1] == "(":
            ans += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if stack[i - 1] == "[":
            ans += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)
