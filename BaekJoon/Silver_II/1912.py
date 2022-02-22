from sys import stdin


n = int(stdin.readline().rstrip())
num = list(map(int,stdin.readline().rstrip().split()))

dp = [0] * (n)
dp[0] = num[0]

for i in range(1,len(num)):
    dp[i] = max(num[i],dp[i-1]+num[i])
    
print(max(dp))
 
        


        

