import sys

input = sys.stdin.readline

n = int(input().rstrip())    
k = int(input().rstrip())    
graph = [[0]*n for i in range(n)]
for _ in range(k):
    a,b = map(int,input().rstrip().split())
    graph[a-1][b-1] = 1
l = int(input().rstrip())    
query = []
for _ in range(l):
    a,b = input().rstrip().split()
    query.append([int(a),b])
    
# n,k,l = 6,3,3
# graph = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# query = [[3, 'D'], [15, 'L'], [17, 'D']]

# 우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]




def simul():
    time = 0
    now_x,now_y = 0,0       # 현재위치
    now_dir = 0             # 현재방햘
    index = 0               # query의 index
    graph[now_x][now_y] = 2 # 몸통,꼬리 2로표시
    q = [(now_x,now_y)]
    
    while True:
        nx = now_x + dx[now_dir]
        ny = now_y + dy[now_dir]
        
        
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 2:
            if graph[nx][ny] == 0:      # 빈 곳일 때
                q.append((nx,ny))
                graph[nx][ny] = 2       
                px,py = q.pop(0)        
                graph[px][py] = 0       # 꼬리 자르기
            if graph[nx][ny] == 1:      # 사과 일 때
                q.append((nx,ny))
                graph[nx][ny] = 2
        else:
            time += 1
            break
        time += 1
        now_x,now_y = nx,ny
        
        if index < l and time == query[index][0]:       # 회전
            if query[index][1] == 'D':
                now_dir = (now_dir + 1) % 4
            else:
                now_dir = (now_dir - 1) % 4
            index += 1
    return time


print(simul())


        
        
    


    
    
    



    