# 여행가 A는 N x N 크기의 정사각형 공간 위에 있다.
# 가장 왼쪽 좌표는 (1, 1)이며, 가장 오른쪽 좌표는 (N, N)이다.
# 여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며,
# 시작 좌표는 (1, 1)이다.
# 계획서에는 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위쪽으로 한 칸 이동
# D : 아래쪽으로 한 칸 이동
# 이 때, A가 N x N 크기의 정사각형 공간을 벗어나는 움직이는 무시된다.
# 예를 들어 (1, 1)의 위치에서 L 또는 U를 만나면 무시된다.

# 입력 예시
# 5
# R R R U D D
# 출력 예시
# 3 4

###############################################
# 나의 풀이
# n = int(input())
# data = input().split()
# move = ['L','R','U','D']
# n = 5
# x, y = 1, 1
#     # 동, 북, 서, 남
# dx = [0, -1, 0, 1]      # 위(-1), 아래(+1)
# dy = [1, 0, -1, 0]      # 왼쪽(-1), 오른쪽(+1)

# for i in range(n-1):
#     for j in move:
#         if j == 'L':
###############################################
# 풀이

n = int(input())
plans = input().split()
x ,y = 1, 1

# L, R, U, D에 따른 이동 방향 (방향 벡터)
#    동  서  남  북
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L','R','U','D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)












###############################################
