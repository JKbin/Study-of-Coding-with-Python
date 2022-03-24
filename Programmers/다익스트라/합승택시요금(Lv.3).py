import heapq

n,s,a,b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	

INF = int(1e9)

def solution(n,s,a,b,fares):
    answer = 0
    
    graph = [[]for i in range(n+1)]     # 그래프 정의
    
    # 양방향 그래프 정의
    for x,y,z in fares:
        graph[x].append((y,z))
        graph[y].append((x,z))
        
    # start -> end 까지의 최단 경로 구하기 (다익스트라)
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
    
    
    # s -> a 까지의 최단경로 + s -> b 까지의 최단경로
    answer = fun(s,a) + fun(s,b)
    
    # i를 거쳐서 가는 최단 경로
    for i in range(1,n+1):
        answer = min(answer, fun(s,i)+fun(i,a)+fun(i,b))
    return answer


print(solution(n,s,a,b,fares))


    
    
                    
            
            
                       
        

