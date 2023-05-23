# 트리에서의 DP

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

# dp[i][0] : 내가 얼리어답터가 아닌 경우 -> 자식노드는 무조건 얼리어답터여야한다.
# dp[i][1] : 내가 얼리어답터인 경우 -> 자식노드가 얼리어답터여도 되고, 아니여도 된다.
dp = [[0, 1] for _ in range(n+1)]

def dfs(now):
    visited[now] = 1
    
    for next_node in graph[now]:
        if not visited[next_node]:
            dfs(next_node)
            # 내가 얼리어답터인 경우
            dp[now][1] += min(dp[next_node][0], dp[next_node][1])
            # 내가 얼리어답터가 아닌 경우
            dp[now][0] += dp[next_node][1]
    #dp[now][1] += 1
        
dfs(1)
print(min(dp[1][0], dp[1][1]))









