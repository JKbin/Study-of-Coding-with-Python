# pypy3으로 제출

from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph = []

for _ in range(n):
    graph.append(list(map(str,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]




def bfs(i,j):    
    q.append((i,j))
    dist = [[0]*m for i in range(n)]
    dist[i][j] = 1
    check = 0

    while q:
        
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 'L' and dist[nx][ny] == 0:
                    q.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1
                    check = max(check,dist[nx][ny])
    return check-1
                    
q = deque()
answer = 0                  
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            answer = max(bfs(i,j),answer)
            
print(answer)

            
                    
    
                    
                
    
    
            
    

            
                
    
    

