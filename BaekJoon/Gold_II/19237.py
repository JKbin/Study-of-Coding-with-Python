# 1. 인접한 칸 중 냄새가 없는 칸, 상어의 방향 우선순위대로 이동
# 2. 냄새가 없는 칸이 없는 경우 : 우선순위대로 이동

import sys

# 1,2,3,4 : 상하좌우
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

input = sys.stdin.readline
n,m,k = map(int,input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
sharks_dir = list(map(int,input().rstrip().split()))
sharks_dir.insert(0,0)
priority = dict()
for i in range(1,m+1):
    priority[i] = [[0]]
idx = 1
while idx <= m:
    for _ in range(4):
        data = list(map(int,input().rstrip().split()))
        priority[idx].append(data)
    idx += 1
grp = [[[0,0] for i in range(n)] for i in range(n)]         # 상어번호, 냄새





for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            grp[i][j] = [graph[i][j],k]

table = dict()                                              # 상어의 현재 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            table[graph[i][j]] = [i,j]
            

time = 0
d_sharks = 0
chk = False
while time < 1000:
    time += 1
    move_tmp = []                                           # 이동할 상어들
    for shark_num in range(m,0,-1):                         # 상어의 번호가 높은 순서대로(잡아먹히는거 신경안써도됨)
        v = table[shark_num]
        move_chk = False
        
        if v != None:
            sdir = sharks_dir[shark_num]                    # 현재 상어 방향
            sx,sy = v[0],v[1]                               # 현재 상어 위치
            move = priority[shark_num][sdir]                # 해당 상어의 이동우선순위
            
            for i in move:
                nx = sx + dx[i]
                ny = sy + dy[i]
                ndir = i
                
                if 0<=nx<n and 0<=ny<n:
                    if grp[nx][ny] == [0,0]:        # 빈칸 존재 시
                        move_tmp.append([shark_num,nx,ny,ndir])     
                        graph[sx][sy] = 0
                        move_chk = True
                        break
            
            if not move_chk:                         # 빈칸 없을 때
                move = priority[shark_num][sdir]
                
                for i in move:                      # 이동우선순위대로
                    nx = sx + dx[i]
                    ny = sy + dy[i]
                    ndir = i
                    
                    if 0<=nx<n and 0<=ny<n:
                        if grp[nx][ny][0] == shark_num:     # 자기 냄새 찾아가기
                            move_tmp.append([shark_num,nx,ny,ndir])
                            graph[sx][sy] = 0
                            break
                
                
                        
    # 상어 이동
    if move_tmp:
        for s_num,x,y,d in move_tmp:
            table[s_num] = [x,y]
            grp[x][y] = [s_num,k]
            sharks_dir[s_num] = d
            
            if graph[x][y] > 0:
                d_sharks += 1
                table[graph[x][y]] = None
            graph[x][y] = s_num
            
    
    # 냄새 없애기
    for i in range(n):
        for j in range(n):
            if [i,j] not in list(table.values()):
                if grp[i][j][1] > 1:
                    grp[i][j][1] -= 1
                elif grp[i][j][1] == 1 and grp[i][j][0] > 0:
                    grp[i][j] = [0,0]
    
    if d_sharks >= m - 1:
        for key in table:
            if key == 1:
                if table[key] != None:
                    chk = True
    
    if chk:
        break
    
if not chk:
    print(-1)
else:
    print(time)
                        
                        
                        
                
                
                        
                        
                    

        
        
        
        
        
        
        
    
    







        
    






