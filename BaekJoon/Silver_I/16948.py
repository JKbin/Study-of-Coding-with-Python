from collections import deque
from sys import stdin


# m,n = map(int,stdin.readline().rstrip().split())
n = int(stdin.readline().rstrip())
start1,start2,end1,end2 = map(int,stdin.readline().rstrip().split())

graph = [ [0]*n for i in range(n) ]
visited = [ [False]*n for i in range(n) ]

# 6,6
# 0,1

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x,y):
    
    q = deque()
    q.append((x,y))
    
    while q:
        
        x,y = q.popleft()
        visited[x][y] = True
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                visited[nx][ny] = True
                
bfs(start1,start2)

if graph[end1][end2] == 0:
    print(-1)
else:                
    print(graph[end1][end2])



    
    


        
        
        
        


