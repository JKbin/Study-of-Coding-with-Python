import heapq
import sys
input = sys.stdin.readline

# 프로그래머스 합승택시요금 문제

# 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우

INF = int(1e9)

#n,m = map(int,input().split())
#start = int(input())
n,m = 6,11
start = 1
#graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
# for i in range(m):
#     a,b,c = map(int,input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph[a].append((b,c))
    
graph = [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

def dijkstra(start):
    q = []
    
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
                
            
    

