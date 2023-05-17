# 다익스트라 경로 역추적해서
# 가장 긴 cost 경로 빼기

import sys, heapq

INF = float('inf')

input = sys.stdin.readline

n, s, e = map(int, input().rstrip().split())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    paths = [start] * (n+1)
    heapq.heappush(q, (start, 0))       # 노드, 비용
    
    while q:
        now, dist = heapq.heappop(q)
        
        if distance[now] < dist : continue
        
        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if distance[next_node] > cost:
                distance[next_node] = cost
                paths[next_node] = now
                heapq.heappush(q, (next_node, cost))
                
    return distance, paths


d, p = dijkstra(s)

# 경로 찾기
ans = []
temp = e
while temp != s:
    ans.append(temp)
    temp = p[temp]
    
ans.append(s)
ans.reverse()

tp = []
for i in range(1, len(ans)):
    prev = ans[i-1]     # 1
    now = ans[i]        # 2
    
    for node, cost in graph[prev]:
        if node == now:
            tp.append(cost)
if not tp:
    print(d[e])
else:
    print(d[e]-max(tp))


            
        
    
    
    


