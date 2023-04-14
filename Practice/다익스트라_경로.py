# BOJ 11779

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[]for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))
    
start, end = map(int , input().rstrip().split())


def dijkstra(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0                 # 방문 표시
    path = [start] * (n+1)
    
    q = []
    heapq.heappush(q, (0, start))       # 비용, 노드
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: continue
        
        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                path[next_node] = now
                
    return distance, path


distance, path = dijkstra(start, end)

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = path[tmp]
ans.append(str(start))
ans.reverse()


print(distance[end])
print(len(ans))
print(' '.join(ans))

    

    