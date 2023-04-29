# dp 기본문제 
# LCS (최장 공통 부분 수열)

import sys

input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

#word1 = 'ACAYKP'
#word2 = 'CAPCAK'

n = len(word1)      # 행
m = len(word2)      # 열

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 끝자리가 같다면 대각선 왼쪽 위에서 +1
        if word1[i-1] == word2[j-1]:        
           dp[i][j] = dp[i-1][j-1] + 1
        # 끝자리가 다르다면 max(위, 왼쪽)
        else:                           
           dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

