# LCS2

import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

#s1 = 'ABCDEF'
#s2 = 'BEFDEFACDFABZ'

n = len(s1)     # 6
m = len(s2)     # 6

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


# dp 채우기
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


if dp[-1][-1] == 0:
    print(0)
else:
    print(dp[-1][-1])
    
    x, y = n, m
    now = dp[-1][-1]
    res = ''
    
    # 현재 값과 위쪽 값-1, 왼쪽 값-1이 같으면 좌상 대각선으로 이동
    while dp[x][y] != 0:
        if dp[x-1][y] == now - 1 and dp[x][y-1] == now - 1:
            res += s1[x-1]
            x -= 1
            y -= 1
            now -= 1
        else:
            # 위가 더 큰 경우
            if dp[x-1][y] > dp[x][y-1]:
                x -= 1
            else:
                y -= 1
    
    print(res[::-1])
