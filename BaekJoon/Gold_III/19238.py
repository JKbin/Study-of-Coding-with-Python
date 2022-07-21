from collections import deque
import sys

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,k = map(int,input().rstrip().split())       # k : 초기연료
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
now_x,now_y = map(int,input().rstrip().split())
guests = dict()
for _ in range(m):
    data = list(map(int,input().rstrip().split()))
    x,y,a,b = data[0]-1,data[1]-1,data[2]-1,data[3]-1
    guests[(x,y)] = [a,b]
now_x -= 1
now_y -= 1


# n,m,k = 6,3,15
# graph = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0]]
# now_x,now_y = 5,4
# guests = {(1, 1): [4, 5], (4, 3): [0, 5], (3, 1): [2, 4]}

    

# 현재위치에서 최단거리 찾기 + 제일 가까운 손님 찾기
def find():
    dist = [[-1]*n for i in range(n)]
    q = deque()
    q.append([now_x,now_y])
    dist[now_x][now_y] = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])
    
    tmp = []
    for i in guests.keys():
        a,b = i[0],i[1]
        tmp.append([a,b,dist[a][b]])
    tmp.sort(key=lambda x:(x[2],x[0],x[1]))     # 거리,행,열 작은 순서로 정렬
    z = tmp[0]
    return z[0],z[1],z[2]

# 도착지까지의 거리 계산
def arrive(arr):
    dist = [[-1]*n for i in range(n)]
    a,b = arr
    dist[now_x][now_y] = 0
    
    q = deque()
    q.append([now_x,now_y])
    
    while q:
        
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1 and graph[nx][ny] != 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
    return dist[a][b]

    
    
chk = True  
                
while guests:
    
    value = find()
    guest_x,guest_y,need_k = value      # 가장 가까운 손님의 거리, 필요 연료
    
    # 연료가 없으면 종료 or 도착지까지 도착못할 경우 종료
    if k < need_k or need_k == -1:
        chk = False
        break
    
    k -= need_k
    now_x,now_y = guest_x,guest_y
    
    arr_k = arrive(guests[(now_x,now_y)])       # 손님 태웠으니 도착지까지 거리 계산
    if arr_k > k:
        chk = False
        break
    
    k -= arr_k
    k += (arr_k*2)      # 연료 충전
    
    
    now_x,now_y = guests[(now_x,now_y)]           # 현재 위치 갱신
    guests.pop((guest_x,guest_y))               # 게스트 삭제
    

print(k) if chk else print(-1)

    
    
    
    
    
    
    
    
    

    
    
    
    
    

