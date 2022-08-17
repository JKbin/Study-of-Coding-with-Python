from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,v = map(int,input().rstrip().split())    
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
    
# 바이러스를 놓을 수 있는 공간 확인
viruses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses.append((i,j))
    
        
def bfs(p_virus,graph):
    time = [[0]*n for i in range(n)]            # 시간을 저장할 변수
    
    for x1,y1 in viruses:                       # 모든 바이러스의 경우의 수 - combination 바이러스 경우의 수 (나머지는 벽으로 처리)
        if (x1,y1) not in p_virus:
            graph[x1][y1] = 0
            
    q = deque()
    for i in p_virus:
        x1,y1 = i
        q.append((x1,y1))
        
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0 and time[nx][ny] == 0:
                    q.append((nx,ny))
                    time[nx][ny] = time[x][y] + 1
    
    # 바이러스가 다 퍼졌는지 체크
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 2 and graph[i][j] != 1:       # 바이러스 and 벽이 아닌데 time == 0인 경우는 다 퍼뜨리지 못한 경우
                if time[i][j] == 0:
                    return -1
    # 시간 구하기
    t_max = 0
    for i in range(n):
        for j in range(n):
            if time[i][j] > 0:
                t_max = max(t_max,time[i][j])
    
    return t_max
    
                
res = []
for i in combinations(viruses,v):           # 바이러스를 놓을 수 있는 모든 경우의 수 check
    grp = deepcopy(graph)
    value = bfs(i,grp)
    if value != -1:
        res.append(value)

if not res:
    print(-1)
else:
    print(min(res))
    
    




        
    
    
    
    






    
    
    
        
        



