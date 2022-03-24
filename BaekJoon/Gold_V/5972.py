# 다익스트라

import sys,heapq

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().rstrip().split())

graph = [[]for i in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):
    a,b,c = map(int,input().rstrip().split())
    graph[b].append((a,c))
    graph[a].append((b,c))
    
    
    
def fun(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    
    while q:
        
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist: continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
fun(1)

print(distance[n])



    
    



