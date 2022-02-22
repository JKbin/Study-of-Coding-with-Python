n = 5
x,y = 1,1
plans = ['R','R','R','U','D','D']

# L,R,U,D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0,]
move_type = ['L','R','U','D']


for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)