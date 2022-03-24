import sys,heapq
INF = int(1e9)
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph = [[]for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

k,l = map(int,input().rstrip().split())
    
def fun(start,end):
    distance = [INF] * (n+1)
    
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist , now = heapq.heappop(q)
        
        if distance[now] < dist: continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]

result = INF
result = min(fun(1,k)+fun(k,l)+fun(l,n),fun(1,l)+fun(l,k)+fun(k,n))

if result >= INF:
    print(-1)
else:
    print(result)
    