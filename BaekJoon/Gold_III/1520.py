# DFS + DP 
# 이미 수행한 경로를 저장해서 시간 단축하는 방법
# 상하좌우 다 활용해야함
# 하좌우만 했을 때 틀림

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

#n, m = 4, 5
#graph = [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

# 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

dp = [[-1]*m for i in range(n)]

def dfs(a,b):
    
    if [a,b] == [n-1,m-1]:
        return 1
    
    if dp[a][b] == -1:
        
        dp[a][b] = 0
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] < graph[a][b]:
                    dp[a][b] += dfs(nx,ny)
    
    return dp[a][b]
    

print(dfs(0,0))









