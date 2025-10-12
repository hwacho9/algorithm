strs = ["flower", "flow", "flight"]

v = sorted(strs)

ans = ""
print(v[0][0])

first = v[0]
last = v[-1]
for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
        print(ans)
    ans += first[i]

    # print(ans)


# for i in range(len(strs)):
