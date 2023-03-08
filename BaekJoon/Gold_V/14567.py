# 위상 정렬 문제 (선수 과목)

import sys
from collections import deque   

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[]for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1


#n,m = 6,4
#graph = [[], [2, 3], [5], [], [5], [], []]
#indegree = [0, 0, 1, 1, 0, 2, 0]

res = []

q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append( (i,1) )       # i, cnt

while q:
    now, cnt = q.popleft()
    res.append([now,cnt])
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append((i,cnt+1))

res.sort(key=lambda x:x[0])

for i in res:
    print(i[1],end=' ')
