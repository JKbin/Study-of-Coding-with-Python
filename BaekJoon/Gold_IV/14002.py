# 가장 긴 증가하는 부분 수열
import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

#n = 6
#arr = [10, 20, 10, 30, 20 ,50]

dp = [1] * (n)
result = []
l = 0

for i in range(1, n):
    for j in range(i):
        now = arr[i]
        prev = arr[j]
        if now > prev:
            dp[i] = max(dp[j] + 1, dp[i])
        
            
m = max(dp)
print(m)

# dp에 저장되어 있는 값을 arr과 매칭시켜서 뽑기
for i in range(n-1,-1,-1):
    if dp[i] == m:
        result.append(arr[i])
        m -= 1

result.reverse()
print(*result)
    
    



            
            
        
        
    


