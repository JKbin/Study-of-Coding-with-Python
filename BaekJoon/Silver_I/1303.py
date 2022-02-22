from collections import deque
from sys import stdin


m,n = map(int,stdin.readline().rstrip().split())
#m,n = 5,5

graph = []
#graph = [['w', 'b', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['b', 'b', 'b', 'b', 'b'], ['b', 'b', 'b', 'w', 'w'], ['w', 'w', 'w', 'w', 'w']]
for i in range(n):
    graph.append(list((map(str,stdin.readline().rstrip()))))

visited = [ [False]*m for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color):
    
    q = deque()
    q.append((x,y,color))
    visited[x][y] = True
    cnt = 0
    
    while q:
        
        x,y,color = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == color:
                if visited[nx][ny] == False:
                    q.append((nx,ny,graph[nx][ny]))
                    visited[nx][ny] = True
                    cnt += 1
                
    return cnt+1

white = 0
blue = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 'W':
            white += (bfs(i,j,graph[i][j]))**2
        elif not visited[i][j] and graph[i][j] == 'B':
            blue += (bfs(i,j,graph[i][j]))**2
            
print(white,blue)


            
    

    
    
    
    
    
    
