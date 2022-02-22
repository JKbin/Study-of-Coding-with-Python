import sys
from collections import deque

m,n,h = map(int,sys.stdin.readline().rstrip().split())
graph = []
q = deque()

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int,sys.stdin.readline().rstrip().split())))
        for k in range(m):
            if temp[j][k] == 1:
                q.append((i,j,k))
    graph.append(temp)
    


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]



def bfs():
    while q:
        x,y,z = q.popleft()
        
    
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
        
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                q.append((nx,ny,nz))
            
bfs()
#print(graph)

day = []

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
        day.append(max(graph[i][j]))
        
print(max(day)-1)
            


            
            
        



    
            
        
        


        
        
    
