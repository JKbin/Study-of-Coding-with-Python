# 위상 정렬

import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())        
graph = [[] for i in range(n+1)]    
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

res = []

# deque 대신 heapq 사용!
q = []
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)

while q:
    now = heapq.heappop(q)
    res.append(now)
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q,i)


for i in res:
    print(i, end=' ')


    
                

    