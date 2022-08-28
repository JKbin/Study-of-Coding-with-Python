# 격자에는 크기가 큰 상어 1마리만 존재가능



import sys
input = sys.stdin.readline

# 상하우좌(1234)
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
reverse_dir = {1:2, 2:1, 3:4, 4:3}

graph = []
n,m,k = map(int,input().rstrip().split())
graph = [[[0,0,0,0]for i in range(m)] for i in range(n)]          # [상어번호,속력,방향,크기]
table = dict()
for i in range(k):
    data = list(map(int,input().rstrip().split()))
    x,y,s,d,z = data[0],data[1],data[2],data[3],data[4]
    graph[x-1][y-1] = [i+1,s,d,z]
    table[i+1] = [x-1,y-1]
    
# 상어에 대한 정보 (r,c,s,d,z) 
# r,c : 상어의 위치
# s : 상어의 속력
# d : 이동방향
# z : 크기

# 낚시왕의 위치에서 상어를 잡는 함수
def catch(hx):
    for i in range(n):
        if graph[i][hx] != [0,0,0,0]:
            return [i,hx,graph[i][hx]]
    return None


# 상어의 움직임
def move():
    
    move_tmp = []
    grp = [[[0,0,0,0]for i in range(m)] for i in range(n)]          # [상어번호,속력,방향,크기]
    
    for shark_num in table:
        if table[shark_num] != None:
            sx,sy = table[shark_num]                    # 상어의 현재위치
            info = graph[sx][sy]                        # 상어의 정보
            speed,dir,size = info[1],info[2],info[3]    # 속력,방향,사이즈
            
            if speed == 0:                              # 속력이 0일 때 nx,ny 갱신
                nx,ny = sx,sy
            
            for i in range(speed):
                nx = sx + dx[dir]
                ny = sy + dy[dir]
                
                if 0<=nx<n and 0<=ny<m:                 # 범위 내에 있으면
                    sx,sy = nx,ny                       # 현재위치로 갱신
                else:                                   # 범위 안에 없으면
                    dir = reverse_dir[dir]              # 방향 반대로하고 계속진행
                    
                    nx = sx + dx[dir]
                    ny = sy + dy[dir]
                    sx,sy = nx,ny
            move_tmp.append([shark_num,speed,dir,size,nx,ny])               # 동시에 움직이니깐 move_tmp라는 배열에 이동할 수 있는 상어 일단 저장
    
    if move_tmp:
        for snum,sp,d,s,x,y in move_tmp:
            if s > grp[x][y][3] :                                           # 사이즈가 큰 상어만 grp에 저장
                grp[x][y] = [snum,sp,d,s]
                table[snum] = [x,y]
            
    return grp

            
            
                    
            
                

total_size = 0
hx = -1         # 낚시왕의 위치

for _ in range(m):
    
    hx += 1         # 오른쪽으로 한칸 이동
    
    v = catch(hx)
    if v != None:
        sx,sy,info = v          # info : 상어번호,속력,방향,크기
        table[info[0]] = None   # 상어잡힘
        total_size += info[3]
        graph[sx][sy] = [0,0,0,0]
    
    graph = move()
    
print(total_size)

    
        
        
        
        
        
    
    
    
    
    
    

    
        
        

