# 다익스트라, BFS

import sys, heapq
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

while 1:
    n, m = map(int, input().rstrip().split())
    if n == 0:
        break
    start, end = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append([b,c])
        reverse_graph[b].append([a,c])
    drop = [[False for _ in range(n+1)] for _ in range(n+1)]        # 최단 거리 경로를 check하는 변수
    
    # 최단 거리 찾기, 최단 경로 check
    def dijkstra():
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))       # 비용, 노드
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist : continue
            
            for next_node, next_cost in graph[now]:
                cost = next_cost + dist
                
                if cost < distance[next_node] and not drop[now][next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
    
    # 최단 거리 역추적해서 최단 거리 막기 (drop)
    def bfs():
        q = deque()
        q.append(end)
        
        while q:
            now = q.popleft()
            
            if now == start:
                continue
            
            for prev, cost in reverse_graph[now]:
                if distance[now] == cost + distance[prev]:
                    if not drop[prev][now]:                 # 방문 체크!!
                        q.append(prev)
                        drop[prev][now] = True
    
    distance = [INF] * (n+1)
    dijkstra()
    bfs()
    distance = [INF] * (n+1)
    dijkstra()
    
    if distance[end] == INF:
        print(-1)
    else:
        print(distance[end])
    
    
    
    
    
                
                
    
        

