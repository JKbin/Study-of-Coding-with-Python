import sys,heapq

input = sys.stdin.readline
INF = sys.maxsize           # INF값 설정을 sys.maxsize로 할 것

n,m = map(int,input().rstrip().split())
ward = list(map(int,input().rstrip().split()))
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
distance = [INF] * (n+1)
ward[-1] = 0                # 마지막 분기점은 통과 가능




def fun(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    
    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist: continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if ward[i[0]] == 0:                 # 분기점이 통과가능한지 check
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
                    
                
                
fun(0)

if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n-1])
    





    
    
