from collections import deque
import sys
input = sys.stdin.readline

# 구현문제, 방향, 최대한 변수 적게 만들 것

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

dx1 = [-1,1,1,-1]
dy1 = [-1,-1,1,1]




n,m = map(int,input().rstrip().split())
graph = []
query = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
for _ in range(m):
    query.append(list(map(int,input().rstrip().split())))

# n,m = 5,4
# graph = [[0, 0, 1, 0, 2], [2, 3, 2, 1, 0], [4, 3, 2, 9, 0], [1, 0, 2, 9, 0], [8, 8, 2, 1, 0]]
# query = [[1, 3], [3, 4], [8, 1], [4, 8]]



# 처음 구름 위치
clouds = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]

while query:
    dir,move = query.pop(0)
    after_clouds = []
    
    
    # 구름 움직이기 (중요!)
    for i in clouds:
        x,y = i
        nx = (n+x+(dx[dir]*move)) % n       # 나머지 연산
        ny = (n+y+(dy[dir]*move)) % n
        after_clouds.append((nx,ny))
    
    # 구름이 있는 곳 강수량 1씩 증가
    visited = [[False]*n for i in range(n)]
    for c in after_clouds:
        x1,y1 = c
        graph[x1][y1] += 1
        visited[x1][y1] = True
        
    # 대각선 체크
    q = deque(after_clouds)
    while q:
        x,y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx1[i]
            ny = y + dy1[i]
            
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] >= 1:
                    cnt += 1
        graph[x][y] += cnt
    clouds = []
    # 구름 만들기
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and visited[i][j] == False:
                graph[i][j] -= 2
                clouds.append((i,j))
    
    
# 최종결과값
res = 0
for i in range(n):
    res += sum(graph[i])
        
print(res)

                   
                
    