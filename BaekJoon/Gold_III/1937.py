# DFS + DP 문제

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

#n = 4
#graph = [[14, 9, 12, 10], [1, 11, 5, 4], [7, 15, 2, 13], [6, 3, 16, 8]]
dp = [[0]*n for i in range(n)]

def dfs(a,b):
    
    # 방문 한 곳이면 그냥 return
    if dp[a][b]:        # if dp[a][b] == 1: 로 하면 시간초과 뜸 -> 왜 그런지는 모르겠음.
        return dp[a][b]
    
    # 방문 표시
    dp[a][b] = 1
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        if 0<=nx<n and 0<=ny<n and graph[a][b] < graph[nx][ny]:
            dp[a][b] = max(dp[a][b], dfs(nx,ny) + 1)
    
    return dp[a][b]
            
ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))
        
print(ans)