# 플로이드 워셜 + 백트래킹

import sys

INF = int(1e9)

input = sys.stdin.readline

n, start = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    
# 플로이드-워셜 수행
for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

answer = sys.maxsize

def dfs(start, cnt, cost):
    global answer
    
    if cnt == n:
        answer = min(answer, cost)
        return
    
    for nxt in range(n):
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, cnt+1, cost+graph[start][nxt])
            visited[nxt] = False
    
visited = [False] * (n+1)
visited[start] = True           # 출발지는 방문처리

# 백트래킹해서 가장 최소시간 구하기
dfs(start, 1, 0)          # 출발지, visited, 방문한 카운트
print(answer)
