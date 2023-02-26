# BFS, 범위 설정, appendleft

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

#n,k = 5, 17

MAX = 100_001

visited = [-1 for _ in range(MAX)]
q = deque()
q.append(n)
visited[n] = 0

while q:
    x = q.popleft()
    
    if x == k:
        print(visited[x])
        break
    
    if (0<= x-1 < MAX) and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
        
    if (0< 2*x < MAX) and visited[2*x] == -1:
        q.appendleft(2*x)
        visited[2*x] = visited[x]
    
    if (0<= x+1 < MAX) and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
    
    


    
    
            
        
        


