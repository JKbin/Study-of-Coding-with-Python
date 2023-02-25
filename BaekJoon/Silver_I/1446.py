# 최단거리 문제 bfs, 다익스트라 

# import heapq
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# n,d = map(int, input().rstrip().split())

# graph = [[]for _ in range(d+1)]
# distance = [INF] * (d+1)
# for i in range(d):
#     graph[i].append((i+1,1))
    
# for i in range(n):
#     s,e,l = map(int,input().rstrip().split())
#     if e > d:
#         continue
#     graph[s].append((e,l))

# def fun(start):
#     distance[start] = 0
#     q = []
#     heapq.heappush(q,(0,start))
    
#     while q:
#         dist, now = heapq.heappop(q)
        
#         if distance[now] < dist: continue
        
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost,i[0]))

# fun(0)
# print(distance[d])


import sys
from collections import deque

input = sys.stdin.readline

n, d = map(int, input().rstrip().split())
roads = []
for _ in range(n):
    start, end, kilo = map(int, input().rstrip().split())
    if end > d:
        continue
    roads.append( (start,end,kilo) )
    

#n,d = 5, 150
#roads = [(0, 50, 10), (0, 50, 20), (50, 100, 10), (110, 140, 90)]

q = deque()
# 현재거리, 누적거리
q.append( (0,0) )
ans = sys.maxsize


while q:
    x,y = q.popleft()
    
    if x == d:
        ans = min(ans, y)
        continue
    
    # 지름길을 타는 경우
    for start,end,kilo in roads:
        if x == start:      # 현재 있는 곳이 지름길의 출발과 같은 경우
            nx = end
            ny = y + kilo
            q.append((nx,ny))
        elif x < start:     # 지름길까지 가는 경우
            nx = start
            ny = y + (start-x)
            q.append((nx,ny))
    
    # 바로 목적지 까지 가는 경우
    if x <= d:
        ny = y+(d-x)
        q.append((d,ny))
        
print(ans)