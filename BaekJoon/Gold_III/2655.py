# 가장 긴 증가하는 부분 수열 (LIS) 심화문제
# 마지막 테이블을 역추적하여 idx 찾기

import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = []
# index, 넓이(area), 높이(height), 무게(weight)
array.append([0,0,0,0])
for i in range(1, n+1):
    a, h, w = map(int, input().rstrip().split())
    array.append([i, a, h, w])
# 무게 순으로 정렬
array.sort(key=lambda x:x[3])

#n = 5
## idx, area, height, weight
#array = [[0, 0, 0, 0], [5, 1, 5, 2], [3, 9, 2, 3], [1, 25, 3, 4], [4, 16, 2, 5], [2, 4, 4, 6]]

dp = [0] * (n+1)

# 현재 area와 0 ~ i-1까지의 area 전부 비교
for i in range(1, n+1):
    for j in range(i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j]+array[i][2])
            
max_value = max(dp)
idx = n
res = []

# 역추적해서 번호 찾기
while idx > 0:
    if max_value == dp[idx]:
        max_value -= array[idx][2]
        res.append(array[idx][0])
    idx -= 1
    
print(len(res))
for i in reversed(res):
    print(i)
    


            
    

    
    






