import heapq
import sys

# 다익스트라 적용
dx = [-1,1,0,0]
dy = [0,0,-1,1]


input = sys.stdin.readline
INF = int(1e9)
              

def fun():
    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0] = 0
    
    while q:
        cost,x,y = heapq.heappop(q)
        
        if x == n-1 and y == n-1:
            print(f'Problem {cnt}: {distance[x][y]}')
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                new_cost = cost + graph[nx][ny]
                
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q,(new_cost,nx,ny))
                    
                    
cnt = 1
    

while True:
    n = int(input().rstrip())
    if n == 0:
        break
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().rstrip().split())))
    distance = [[INF]*(n) for i in range(n)]
    fun()
    cnt += 1
    
    
        