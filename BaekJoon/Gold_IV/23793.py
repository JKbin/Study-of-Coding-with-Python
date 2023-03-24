# 다익스트라, INF 사이즈 int(1e9) -> sys.maxsize로 바꿨음

import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().rstrip().split())    
graph = [[]for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))
x, y, z = map(int, input().rstrip().split())


def fun_1(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))       # 비용, 노드
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[end]

def fun_2(start, end, y):
    distance = [INF] * (n+1)
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0,start))        # 비용, 노드
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if i[0] == y:           # y경로 무시
                continue
            else:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    return distance[end]

                
                


# x -> y -> z까지 가는 최단 경로
answer1 = fun_1(x, y) + fun_1(y, z)

# x -> z까지 가는 최단 경로(y는 거치면 안됨)
answer2 = fun_2(x, z, y)



if answer1 >= INF:
    print(-1, end=' ')
else:
    print(answer1, end=' ')

if answer2 == INF:
    print(-1, end=' ')
else:
    print(answer2, end=' ')
    





    
    


    
            
            


    


        

            
        
        


