import sys,heapq

input = sys.stdin.readline

n,m,x = map(int,input().rstrip().split())

INF = int(1e9)

graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().rstrip().split())
    graph[a].append((b,c))
    

def fun(start,end):
    distance = [INF] * (n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    
    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist : continue
        
        for i in graph[now]:
            cost = i[1] + dist
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
    return distance[end]


res = [] 
for i in range(1,n+1):
    res.append(fun(i,x) + fun(x,i))
res.sort()
print(res[-1])


    
    


            
    
    
    
    
    
    




                    
                
    
    
    