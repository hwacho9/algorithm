s = "()"

print(len(list(s)))

for i in range(len(list(s))):
    print(s[i])
    if s[i] == chr(72) and s[i + 1] == chr(73):
        print("y")
