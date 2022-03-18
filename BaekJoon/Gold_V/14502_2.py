from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

input = sys.stdin.readline


m,n = map(int,input().rstrip().split())    
#m,n = 4,6
graph = []
for i in range(m):
    graph.append(list(map(int,input().rstrip().split())))
#graph = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 1. 벽을 세울수 있는 모든 조합
temp = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            temp.append((i,j))

wall = list(combinations(temp,3))

def bfs(k):
    dist = deepcopy(graph)
    q = deque()
    
    # 벽 세우기
    for i in k:
        dist[i[0]][i[1]] = 1
        
    # 바이러스 퍼트리기
    for i in range(m):
        for j in range(n):
            if dist[i][j] == 2:
                q.append((i,j))
                
    while q:
        
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n:
                if dist[nx][ny] == 0:
                    dist[nx][ny] = 2
                    q.append((nx,ny))
                    
    
    # 안정영역 개수 세기
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if dist[i][j] == 0:
                cnt += 1
                
    return cnt
      
result = []
for i in wall:
    result.append(bfs(i))
    
print(max(result))

        