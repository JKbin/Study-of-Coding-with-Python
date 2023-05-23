# 경로를 반대로 저장하여, 면접장소에서 각 도시로 가는 거리를 구한다.

import sys, heapq

input = sys.stdin.readline

INF = float('inf')

n, m, k = map(int, input().rstrip().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    # 경로 반대로 저장
    graph[b].append((a,c))
    
distance = [INF] * (n+1)
q = []

# 면접장들 미리 방문 처리
#l = list(map(int, input().rstrip().split()))
l = set(map(int, input().rstrip().split()))
for i in l:
    distance[i] = 0
    # heapq에 면접장소 먼저 다 넣기
    heapq.heappush(q, (0, i))           # 비용, 노드
    
while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist: continue
    
    for next_node, next_cost in graph[now]:
        cost = dist + next_cost
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

# 거리가 가장 멀고, 도시 번호가 가장 적은 것 찾기
maxValue = max(distance[1:])
answer = []
for i in range(1, n+1):
    if distance[i] == maxValue:
        answer.append((i, distance[i]))
answer.sort(key=lambda x:(-x[1],x[0]))
print(answer[0][0])
print(answer[0][1])


