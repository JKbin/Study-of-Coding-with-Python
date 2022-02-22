from collections import deque
from sys import stdin


#m,n = 3,3

m,n = map(int,stdin.readline().rstrip().split())

graph = []


#graph = [['D', '.', '*'], ['.', '.', '.'], ['.', 'S', '.']]
for i in range(m):
    graph.append(list(map(str,stdin.readline().rstrip())))

# * : 물
# D : 소굴
# S : 고슴도차
# X : 벽


visited = [ [False]*n for i in range(m)]
count = [[0]*n for i in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()

def bfs(Dx,Dy):
    
    while q:
        
        x,y = q.popleft()
        
        if graph[Dx][Dy] == 'S':
            return count[Dx][Dy]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            
            if 0<=nx<m and 0<=ny<n:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    count[nx][ny] = count[x][y] + 1
                    q.append((nx,ny))
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx,ny))
    return "KAKTUS"


            
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'S':
            q.append((i,j))
        elif graph[i][j] == 'D':
            Dx,Dy = i,j
            
for i in range(m):
    for j in range(n):
        if graph[i][j] == '*':
            q.append((i,j))
            
print(bfs(Dx,Dy))
            
            

                    
                    
            

                        
        
            

                    
                
                
            
                
        
    
    
    
    
    
    
    
    
    
    
    