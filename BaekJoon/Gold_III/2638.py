# 가장자리(0)을 q에 넣고 bfs
# 공기 접촉 2 조건 잘 생각할 것

import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    
#n, m = 8, 9 
#graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0], 
#        [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    cnt = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                    cnt += 1
                
    return cnt
                    
time = 0
while True:
    time += 1
    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
            elif graph[i][j] == 2:
                graph[i][j] = 1
    
    
print(time-1)    

    



                
                
            
    
    
    