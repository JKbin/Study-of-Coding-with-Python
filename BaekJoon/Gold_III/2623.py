# 위상 정렬 문제

import sys
from collections import deque   

input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    data = list(map(int, input().rstrip().split()))
    
    idx = 0
    cnt = data[0]
    num_list = data[1:]
    
    while idx < cnt-1:
        now_number = num_list[idx]
        next_number = num_list[idx+1]
        
        indegree[next_number] += 1
        graph[now_number].append(next_number)
        
        idx += 1
        

res = []
q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        

while q:
    now = q.popleft()
    res.append(now)
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(res) != n:
    print(0)
else:
    for i in res:
        print(i)
        
    

    