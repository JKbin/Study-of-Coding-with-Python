import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))


#graph = [[4, 3, 2, 2, 1, 0, 1], [3, 3, 3, 2, 1, 0, 1], [2, 2, 2, 2, 1, 0, 0], [2, 1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 1, 0], [0, 1, 2, 2, 1, 1, 0], [0, 1, 1, 1, 2, 1, 0]]
#n, m = 8, 7

dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]

total = [[False]*m for i in range(n)]

def bfs(i, j):
    visited = [[False]*(m) for i in range(n)]
    visited[i][j] = True
    q = deque()
    q.append([i,j])
    
    while q:
        x,y = q.popleft()
        now = graph[x][y]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == now:
                    if not visited[nx][ny]:
                        q.append([nx,ny])
                        total[nx][ny] = True
                        visited[nx][ny] = True
                elif graph[nx][ny] > now:
                    return False
    
    return True
                    
answer = 0

for i in range(n):
    for j in range(m):
        if bfs(i, j):
            if not total[i][j]:
                answer += 1
            

print(answer)

        

                
                
    
    



        


