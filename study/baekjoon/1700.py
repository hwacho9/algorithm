from sys import stdin

n, k = map(int, stdin.readline().strip().split())
items = list(map(int, stdin.readline().split()))

multiTab = [0] * n
cnt = 0

for i in range(len(items)):

    if items[i] in multiTab:
        continue
    else:
        if 0 in multiTab:
            multiTab[multiTab.index(0)] = items[i]
        else:
            repeat = []
            for j in range(i + 1, len(items)):
                if items[j] in multiTab:
                    repeat.append(items[j])

            if repeat:
                repeat_list = list(dict.fromkeys(repeat))
                for k in range(len(items)):
                    if multiTab[k] not in repeat_list:
                        multiTab[k] = items[i]
                        cnt += 1
                        break

                else:
                    multiTab[multiTab.index(repeat_list[-1])] = items[i]
                    cnt += 1
            else:
                multiTab[0] = items[i]
                cnt += 1

print(cnt)
