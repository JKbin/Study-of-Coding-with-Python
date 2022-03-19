import sys,heapq

input = sys.stdin.readline

K = int(input().rstrip())
INF = int(1e9)


for _ in range(K):


    n,d,start = map(int,input().rstrip().split())


    distance = [INF] * (n+1)
    graph = [[]for i in range(n+1)]
    for i in range(d):
        a,b,c = map(int,input().rstrip().split())
        graph[b].append((a,c))
    

    def fun(start):
        q = []
        distance[start] = 0
        heapq.heappush(q,(0,start))
    
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

    cnt = 0
    time = 0

    for i in distance:
        if i != INF:
            cnt += 1
            time = max(time,i)


    print(cnt,time)
    
            
    
    