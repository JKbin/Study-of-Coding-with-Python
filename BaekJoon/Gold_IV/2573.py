from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
    

# 빙산이 몇개인지 체크
def check(graph):
    visited = [[0]*m for i in range(n)]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visited[i][j] == 0:
                q = deque()
                q.append((i,j))
                visited[i][j] = 1
                
                while q:
                    x,y = q.popleft()
                    
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        
                        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and graph[nx][ny] > 0:
                            visited[nx][ny] = 1
                            q.append((nx,ny))
                cnt += 1
    return cnt
                
           
# 빙산깎기     
def bfs(graph):
    tmp = []
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                q = deque()
                q.append((i,j))
                
                while q:
                    x,y = q.popleft()
                    cnt = 0
                    
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        
                        if 0<=nx<n and 0<=ny<m:
                            if graph[nx][ny] == 0:
                                cnt += 1
                tmp.append([i,j,cnt])
    
    for x1,y1,c1 in tmp:
        if graph[x1][y1] - c1 <= 0:
            graph[x1][y1] = 0
        elif graph[x1][y1] - c1 > 0:
            graph[x1][y1] -= c1
            
    
# 모두 녹는 경우도 있음   
def sum_check(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                return False
    return True                    
            

time = 0

while True:
    v = check(graph)
    
    if v >= 2 and not sum_check(graph):
        print(time)
        break
    elif v < 2 and sum_check(graph):
        print(0)
        break
    
    time += 1
    bfs(graph)
    
    
        


    
