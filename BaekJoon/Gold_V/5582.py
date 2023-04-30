# DP
# LCS 비슷한 문제
# 공통 부분이 이어져야 함.

import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n = len(s1)
m = len(s2)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

answer = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])

print(answer)