import sys
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = []
q = deque([])

#graph = [[1, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, 1]]
#n,m = 6,4


for i in range(m):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append([i,j])
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        x,y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])
            
            
bfs()

result= []
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result.append(max(i)-1)
    
print(max(result))




    
            

            
        
        
    
        
        
            
    

            

    