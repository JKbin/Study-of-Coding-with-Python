import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]
reverse_dir = {0:1, 1:0, 2:3, 3:2}



n,m = map(int,input().rstrip().split())
graph = []
horses = {}                                             # 딕셔너리 : 말의 x,y,dir(방향) 정보 저장
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
for i in range(m):
    a,b,c = map(int,input().rstrip().split())
    horses[i+1] = [a-1,b-1,c-1]
grp = [[[] for i in range(n)] for i in range(n)]        # 배열형식으로 말 저장


for i in horses:
    a,b,c = horses[i]
    grp[a][b].append(i)


cnt = 0
chk = False
while cnt < 1000:
    cnt += 1
    
    for h in horses:
        hx,hy,hdir = horses[h]              # hx,hy : 현재 말의 위치 , hdir : 방향
        idx = grp[hx][hy].index(h)          # 현재 말의 리스트 안의 index
        tmp = []                            # 이동할 말들의 저장하는 변수
        
        
        nx = hx + dx[hdir]                  # 방향대로 이동
        ny = hy + dy[hdir]
        
        if 0<=nx<n and 0<=ny<n:             # 이동한 방향이 범위 안이면?
            if graph[nx][ny] == 0:          # 흰색
                for d in grp[hx][hy][idx:]:
                    tmp.append(d)
            elif graph[nx][ny] == 1:        # 빨간색
                for d in grp[hx][hy][idx:]:
                    tmp.append(d)
                tmp.reverse()
            elif graph[nx][ny] == 2:        # 파란색
                hdir = reverse_dir[hdir]    # 반대방향으로 변경
                nx = hx + dx[hdir]          # 한칸이동
                ny = hy + dy[hdir]
                if 0<=nx<n and 0<=ny<n:     # 범위체크
                    if graph[nx][ny] == 0:
                        for d in grp[hx][hy][idx:]:
                            tmp.append(d)
                    elif graph[nx][ny] == 1:
                        for d in grp[hx][hy][idx:]:
                            tmp.append(d)
                        tmp.reverse()
                    else:                  # 제자리 및 말 위치 갱신
                        nx,ny = hx,hy
                        horses[h] = [hx,hy,hdir]
                else:
                    nx,ny = hx,hy
                    horses[h] = [hx,hy,hdir]
        else:
            hdir = reverse_dir[hdir]
            nx = hx + dx[hdir]
            ny = hy + dy[hdir]
            
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0:
                    for d in grp[hx][hy][idx:]:
                        tmp.append(d)
                elif graph[nx][ny] == 1:
                    for d in grp[hx][hy][idx:]:
                        tmp.append(d)
                    tmp.reverse()
                else:
                    nx,ny = hx,hy
                    horses[h] = [hx,hy,hdir]
                    
        if tmp:                                     # 이동할 말들의 정보
            for v in tmp:                           
                grp[hx][hy].remove(v)               # 현재 자리에서 말 제거
                grp[nx][ny].append(v)               # 이동할 자리에 말 추가
                
                if v == h:                          # 지금 조종하고 있는 말인 경우 방향 체크
                    horses[v] = [nx,ny,hdir]
                else:                               # 업혀져 있는 말들은 자기의 방향대로 넣기
                    tmp_dir = horses[v][2]
                    horses[v] = [nx,ny,tmp_dir]
                    
        if len(grp[nx][ny]) >= 4:
            print(cnt)
            exit()

print(-1)

            

         
        
            
        
        
        
    


            
                
                
            
                    
        
        
    


    
    
    
    
