# 편집거리(edit distance) 알고리즘
# 두 문자열의 유사도를 판단하는 알고리즘
# 수정, 삽입, 삭제 기능이 있다고 할 때 몇 번의 동작이 필요한지 측정한다.

import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

# s1 = 'abcd'
# s2 = 'bcde'

n = len(s1)
m = len(s2)


dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 맨 윗줄 채우기
idx = 0
for i in range(m+1):
    dp[0][i] = idx
    idx += 1
# 맨 왼쪽줄 채우기
idx = 0
for i in range(n+1):
    dp[i][0] = idx
    idx += 1

for i in range(1, n+1):
    for j in range(1, m+1):
        # 만약 두 문자가 같으면 대각선(i-1, j-1) 그대로 내리기
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 그렇지 않으면 위, 왼쪽, 대각선 중 최솟값 + 1
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

print(dp[-1][-1])

            
            

