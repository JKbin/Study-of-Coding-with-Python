from collections import deque
from sys import stdin

m,n = map(int,stdin.readline().rstrip().split())
#m,n = 7,4
graph = []
#graph = [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
for i in range(m):
    graph.append(list(map(int,stdin.readline().rstrip().split())))

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]


q = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i,j))
            

def bfs():
    
    while q:
        
        x,y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
                
                
bfs()


answer = 0

for i in range(m):
    for j in range(n):
        answer = max(answer,graph[i][j])
        
print(answer-1)


            
