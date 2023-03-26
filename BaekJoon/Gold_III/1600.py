# visited를 3차원 배열로 표현
# [x][y][z] 여기서 z는 이동할 수 있는 횟수!! (k 값)

import sys
from collections import deque

input = sys.stdin.readline

# k = int(input().rstrip())
# m, n = map(int, input().rstrip().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().rstrip().split())))
    
# k = 1
# m, n = 4, 4
# graph = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]

k = 2
m, n = 5, 2
graph = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 0]]

monkeys = {
    0: [-1, 0], 
    1: [1, 0],
    2: [0, -1],
    3: [0, 1]
}

horses = {
    0: [2, 1],
    1: [2, -1],
    2: [1, -2],
    3: [-1, -2],
    4: [-2, -1],
    5: [-2, 1],
    6: [-1, 2],
    7: [1, 2],
}


def bfs():
    q = deque()
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

    q.append([0, 0, 0])
    visited[0][0][0] = 1
    
    while q:
        x, y, z = q.popleft()
        
        if [x, y] == [n-1, m-1]:
            return visited[x][y][z]-1
        
        for i in range(4):
            dx = monkeys[i][0]
            dy = monkeys[i][1]
            
            nx = x + dx
            ny = y + dy
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append([nx, ny, z])
                    visited[nx][ny][z] = visited[x][y][z] + 1
        
        if z < k:
            
            for i in range(8):
                dx = horses[i][0]
                dy = horses[i][1]
                
                nx = x + dx
                ny = y + dy
                
                if 0<=nx<n and 0<=ny<m:
                    if graph[nx][ny] == 0 and visited[nx][ny][z+1] == 0:
                        visited[nx][ny][z+1] = visited[x][y][z] + 1
                        q.append([nx, ny, z+1])
    
    return -1
                    
print(bfs())
    
            
