## 27020856 趙聖化

import sys

input = sys.stdin.readline

# indexを合わせるために先頭に0を追加
s1 = [0] + list(input().rstrip())
s2 = [0] + list(input().rstrip())

# dp[x][y]
# 最初の文字列x番目までと2番目の文字列y番目まで比較したとき、LCS長さ

dp = [[0] * len(s2) for _ in range(len(s1))]
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[len(s1) - 1][len(s2) - 1])


"""実行結果

Keyword arguments:
qwert -- maqkwe
Return: 3

abcad -- erabd
Return: 3

abcde -- acbef
Return: 3
"""
