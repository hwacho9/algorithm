S = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


s = input()
print(s[0])
print(len(s))

ans = 0
for i in range(len(s)):
    if i < len(s) - 1 and S[s[i]] < S[s[i + 1]]:
        ans -= S[s[i]]
    else:
        ans += S[s[i]]

print(ans)
