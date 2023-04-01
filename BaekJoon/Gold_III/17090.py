import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
    
answer = 0
dp = [[-1]*m for _ in range(n)] 

dir = {
    'U': [-1, 0],
    'D': [1, 0], 
    'L': [0, -1],
    'R': [0, 1]
}

# n, m = 3, 4
# graph = [['R', 'R', 'D', 'D'], ['R', 'R', 'D', 'R'], ['D', 'U', 'L', 'U']]

def dfs(i, j):
    
    # 범위가 벗어나면 1을 return
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return 1
    
    # 이미 방문한 곳이면 그대로 return
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = 0
    step = graph[i][j]
    
    nx = i + dir[step][0]
    ny = j + dir[step][1]
    
    dp[i][j] = max(dp[i][j], dfs(nx,ny))
    
    return dp[i][j]
    
    
for i in range(n):
    for j in range(m):
        if dp[i][j] == -1:
            if dfs(i, j) == 1:
                answer += 1
        elif dp[i][j] == 1:
            answer += 1

print(answer)

            

 
