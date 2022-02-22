from collections import deque
from copy import copy, deepcopy
from sys import stdin



#m,n = map(int,stdin.readline().rstrip().split())
m,n = 5,7
#graph = []
graph = [[0, 0, 0, 0, 0, 0, 0], [0, 2, 4, 5, 3, 0, 0], [0, 3, 0, 2, 5, 2, 0], [0, 7, 6, 2, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0]]       
# for i in range(m):
#     graph.append(list(map(int,stdin.readline().rstrip().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = deepcopy(graph)

def bfs(i,j,visited):
    q = deque()
    q.append((i,j))
    
    
    if visited[i][j] == 0:
        return False
    
    while q:
        
        x,y = q.popleft()
        
        visited[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n and visited[nx][ny] != 0:
                q.append((nx,ny))
    return True
            
    
result = 0
for i in range(m):
    for j in range(n):
        if bfs(i,j,visited) == True:
            result += 1
            
print(result)




