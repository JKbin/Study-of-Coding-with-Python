# 냅색 알고리즘 (dp)

import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

array = []
array.append([0,0])

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    array.append([a, b])
    
# 무게에 따른 총 가치
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]


for i in range(1, n+1):
   for j in range(1, k+1):
       current = array[i]
       cur_weight, cur_value = current[0], current[1]
       
       # 현재 무게가 j보다 작으면 위(i-1)의 값 그대로
       if j < cur_weight:
           dp[i][j] = dp[i-1][j]
        # max(위의 값, 위의 행에서 j-cur_weight + cur_value 비교)
       else:
           dp[i][j] = max(dp[i-1][j], dp[i-1][j-cur_weight] + cur_value)


print(dp[n][k])
