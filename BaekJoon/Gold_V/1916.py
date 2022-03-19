import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

n = int(input().rstrip())
m = int(input().rstrip())

distance = [INF] * (n+1)

graph = [[]for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().rstrip().split())
    graph[a].append((b,c))
    
start,end = map(int,input().rstrip().split())

def fun(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                

fun(start)

print(distance[end])



    
    
    