from collections import deque
from sys import stdin
import copy

# BFS + 완전탐색


m,n = map(int,stdin.readline().rstrip().split())
#m,n = 4,6
graph = []
#graph = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]
for i in range(m):
    graph.append(list(map(int,stdin.readline().rstrip().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    temp = copy.deepcopy(graph)
    
    for i in range(m):
        for j in range(n):
            if temp[i][j] == 2:
                q.append((i,j))
                
    while q:
        
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx,ny))
                
    global answer
    cnt = 0
    for i in range(m):
        cnt += temp[i].count(0)
    answer = max(answer,cnt)
    
# 벽 만들기
def wall(cnt):
    
    if cnt == 3:
        bfs()
        return
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0
    
answer = 0            
wall(0)
print(answer)

            
    
    