from collections import deque
import sys

input = sys.stdin.readline

n,L,R = map(int,input().rstrip().split())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
    

def bfs(i,j,idx):
    q = deque()
    q.append((i,j))
    united = []         # 연합인 도시들
    united.append((i,j))
    dist[i][j] = idx    # 같은 연합끼리는 inx가 같음
    united_cnt = 1      # 연합의 수
    total = graph[i][j] # 연합의 총합
    
    
    while q:
        
        x,y = q.popleft()
        
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            
            if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    q.append((nx,ny))
                    united.append((nx,ny))
                    united_cnt += 1
                    total += graph[nx][ny]
                    dist[nx][ny] = idx
    
    for x1,y1 in united:
        graph[x1][y1] = total // united_cnt
        
                    
                




res = 0
while True:
    dist = [[-1]*(n)for i in range(n)]

    index = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1:
                bfs(i,j,index)
                index += 1
    
    if index == n*n:
        break
    res += 1
    
    
        
    
print(res)
                
                
            
            