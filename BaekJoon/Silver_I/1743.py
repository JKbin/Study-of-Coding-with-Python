from collections import deque
from sys import stdin

m,n,count = map(int,stdin.readline().rstrip().split())
#m,n,count = 3,4,5
graph = [['.']*n for i in range(m)]
for i in range(count):
    x,y = map(int,stdin.readline().rstrip().split())
    graph[x-1][y-1] = '#'
    
#graph = [['#', '.', '.', '.'], ['.', '#', '#', '.'], ['#', '#', '.', '.']]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [ [False]*n for i in range(m) ]

def bfs(i,j):
    
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    cnt = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] == '#':
                    q.append((nx,ny))
                    cnt += 1
                    visited[nx][ny] = True
                    
    return cnt
            
            
            
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == '#':
            result.append(bfs(i,j))
            
            
print(max(result)+1)

            












