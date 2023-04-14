# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 방향 그래프의 모든 노드를 '방향성에 거슬리지 않도록 순서대로 나열하는 것'
# 시간 복잡도 : O(V+E)
# BOJ 14567

from collections import deque
import sys, heapq                # 문제에 따라 heapq를 사용할 수도 있음

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = [[]for i in range(n+1)]

indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    # 차수 증가
    indegree[b] += 1

q = deque()

res = []

# 차수가 0인 것 먼저 q에 담기
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append((i, 1))
        
while q:
    now, cnt = q.popleft()
    res.append([now, cnt])
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append((i, cnt+1))


res.sort(key=lambda x:x[0])

for i in res:
    print(i[1], end=' ')
    
    
    

    

    
    





                

        
