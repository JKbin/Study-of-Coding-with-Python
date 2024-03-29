from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (n+1)


def dfs(graph,v,visited):
      visited[v] = True
      print(v, end=' ')

      for i in graph[v]:
            if not visited[i]:
                  dfs(graph,i,visited)


def bfs(graph,start,visited):
      visited = [False] * (n+1)
      q = deque([start])
      visited[start] = True


      while q:
            v = q.popleft()
            print(v,end=' ')

            for i in graph[v]:
                  if not visited[i]:
                        q.append(i)
                        visited[i] = True
      




dfs(graph,v,visited)
print()
bfs(graph,v,visited)