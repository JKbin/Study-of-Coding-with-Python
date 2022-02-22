from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

graph = []
for i in range(n):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))
    
#graph = [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*n for i in range(n)]

def bfs(x,y,color):
    
    q = deque()
    q.append((x,y,color))
    
    while q:
        x,y,color = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == color and visited[nx][ny] == False:
                q.append((nx,ny,graph[nx][ny]))
                visited[nx][ny] = True
            
            
cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j,graph[i][j]) 
            cnt += 1
            

visited = [[False]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
            
cnt_2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j,graph[i][j])
            cnt_2 += 1
        
print(cnt)    
print(cnt_2)

            

        
    
    


