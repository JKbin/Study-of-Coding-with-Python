# 다익스트라, heap에 넣는 순서, graph[end]
# 2차원 배열로 distance 초기화 하는 skill

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().rstrip().split())

# 갈 수 있는 거리 : (도착,비용)
graph = [[] for _ in range(v+1)]

# 거리의 최솟값을 저장하는 배열(2차원)
distance = [[INF]*(v+1) for _ in range(v+1)]    

# heapq 배열 선언
q = []

for _ in range(e):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))          # 도착, 비용
    distance[a][b] = c
    # heap을 사용할 것이기 때문에 c(비용)이 맨 앞에 와야함!!!!!
    heapq.heappush(q, (c,a,b))      # 비용, 출발, 도착으로 넣기
    
while q:
    cost,start,end, = heapq.heappop(q)
    
    # heapq을 이용하기 때문에 제일 처음 나온 사이클이 가장 비용이 작은 cycle이다.
    if start == end:
        print(cost)
        break
    
    if distance[start][end] < cost: continue
    
    # start -> end -> ?(ncity) (end에서 갈 수 있는 경로 불러오기)
    for ncity, ncost in graph[end]:          # ncity : 다음도시, ncost : 비용
        new_cost = cost + ncost
        
        # 새로운 비용과 현재의 start -> end -> ncity의 비용 비교
        if new_cost < distance[start][ncity]:
            distance[start][ncity] = new_cost
            heapq.heappush(q, (new_cost, start, ncity))
else:
    print(-1)
    
        
        





        
        

    
    
    