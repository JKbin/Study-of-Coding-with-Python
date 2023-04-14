# 백트래킹

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n, m = map(int, input().rstrip().split())
    if n == 1:
        print(0)
        break
    graph = [[]for i in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().rstrip().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    def dfs(now):
        if not visited[now]:
            visited[now] = True
            
        dynamite = 0
        
        for next_node, next_cost in graph[now]:
            if not visited[next_node]:
                dynamite += min(next_cost, dfs(next_node))
        
        if dynamite:
            return dynamite
        else:
            return 100000           # 다이너마이트 최대 20 보다 큰 값
    
    
    visited = [False] * (n+1)
    visited[1] = True
    print(dfs(1))
    
        