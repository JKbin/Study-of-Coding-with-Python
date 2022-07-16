import sys
input = sys.stdin.readline
# dp
n = int(input().rstrip())
arr = [0]
for _ in range(n):
    arr.append(int(input().rstrip()))        

dp = [0]

dp.append(arr[1])

if n > 1:
    dp.append(arr[1]+arr[2])

# 점화식 찾기(규칙찾기) - 값을 가질 수 있는 조건
for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i]))
    
print(dp[n])

