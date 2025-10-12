from sys import stdin

input = stdin.readline

V, E = map(int, input().split())
root = [i for i in range(V + 1)]
list = []
for _ in range(E):
    list.append(list(map(int, input().split())))


list.sort(key=lambda x: x[2])


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


answer = 0
for s, e, w in list:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            root[sRoot] = eRoot
        else:
            root[eRoot] = sRoot
        answer += w

print(answer)
