from collections import deque
import sys

m,n = map(int,sys.stdin.readline().rstrip().split())
graph = []
for i in range(m):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))


visited = [ [False]*n for i in range(m) ]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    
    global w,s
    
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        
        x,y = q.popleft()
        
        if graph[x][y] == 'v':
            w += 1
        elif graph[x][y] == 'k':
            s += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n and visited[nx][ny] == False and graph[nx][ny] != '#':
                q.append((nx,ny))
                visited[nx][ny] = True
                
                
                
                
wolves = 0
sheeps = 0
    


for i in range(m):
    for j in range(n):
        if graph[i][j] != '#' and visited[i][j] == False:
            w = 0
            s = 0
            bfs(i,j)
            
            if w >= s:
                s = 0
            else:
                w = 0
                
            wolves += w
            sheeps += s
            
        

print(sheeps,wolves)




            
            
            
            
                    
      