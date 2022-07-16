
from collections import deque
from itertools import combinations,chain
import sys

# bfs + combinations, chain(함수) 

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())            
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))

# n,m = 7,3    
# graph = [[2, 0, 2, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0], [2, 1, 0, 0, 0, 0, 2], [1, 
# 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [2, 1, 0, 0, 2, 0, 2]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

viruses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses.append((i,j))
    
res = []
    
def bfs(vis):
    q = deque()
    visit = [[-1]*n for i in range(n)]
    
    for v in vis:
        q.append(v)
        visit[v[0]][v[1]] = 0
        
    max_dist = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1 and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                if graph[nx][ny] == 0:
                    max_dist = max(max_dist,visit[nx][ny])
                q.append((nx,ny))
                
    #temp = list(sum(visit,[]))         # 1차원으로 변환
    temp = list(chain(*visit))          # 1차원으로 변환(chain이 더 빠름)
    # 방문안한 곳과 벽의 개수가 동일한지?
    if temp.count(-1) == list(sum(graph,[])).count(1):
        res.append(max_dist)
    
for vis in combinations(viruses,m):
    bfs(vis)
    
    
print(min(res)) if res else print(-1)



    
            
            
            
    
                    
    
            
        
        
        
        
    



            
            
                    
                    
        
        
        
        
    
    
    
                
                