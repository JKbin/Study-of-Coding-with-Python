import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

for i in range(n):
    m = int(sys.stdin.readline().rstrip())

    graph = []
    for i in range(m):
        graph.append([0] * m)

    x,y = map(int,sys.stdin.readline().rstrip().split())
    w,z = map(int,sys.stdin.readline().rstrip().split())


    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        if x == w and y == z:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    print(graph[w][z])




