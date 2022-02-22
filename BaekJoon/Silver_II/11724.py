import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

visited = [False] * (N + 1)

graph = [ [] for i in range(N+1) ]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph,start,visited):
    visited[start] = True
    q = deque([start])

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(graph,i,visited)
        cnt += 1

print(cnt)


