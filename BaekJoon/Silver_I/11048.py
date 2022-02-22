from sys import stdin




m,n = map(int,stdin.readline().rstrip().split())

graph = []
for i in range(m):
    graph.append(list(map(int,stdin.readline().rstrip().split())))
    
dp = [[0]*(n+1) for i in range(m+1)]





for i in range(1,m+1):
    for j in range(1,n+1):
        dp[i][j] = graph[i-1][j-1] + max(dp[i][j-1],dp[i-1][j],dp[i][j])
        
print(dp[m][n])




        
        
