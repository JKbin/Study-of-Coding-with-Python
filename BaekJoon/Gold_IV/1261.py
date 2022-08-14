
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,input().rstrip())))
    

dist = [[-1]*n for i in range(m)]           # 가중치 계산
dx = [-1,1,0,0]
dy = [0,0,-1,1]


q = deque()
q.append((0,0))
dist[0][0] = 0

while q:
    x,y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<m and 0<=ny<n:
            if dist[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]       # 가중치 x
                    q.appendleft((nx,ny))           # 우선순위가 더 높기 때문에 appendleft
                else:
                    dist[nx][ny] = dist[x][y] + 1   # 가중치 + 1(벽부수기)
                    q.append((nx,ny))
                    
print(dist[m-1][n-1])


                    
            






















    
    




    
    
    




        
    
        
    
    
    
    






    
        
    
    
    
    

    

