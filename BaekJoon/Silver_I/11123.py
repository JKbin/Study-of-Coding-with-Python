from collections import deque
import sys

k = int(sys.stdin.readline().rstrip())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == '#' and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True

for i in range(k):
    m,n = map(int,sys.stdin.readline().rstrip().split())
    
    graph = []
    for i in range(m):
        graph.append(list(map(str,sys.stdin.readline().rstrip())))
        
    visited = [ [False]*n for i in range(m) ]
    
    answer = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == '#' and visited[i][j] == False:
                bfs(i,j)
                answer += 1
                
    print(answer)
    
    
