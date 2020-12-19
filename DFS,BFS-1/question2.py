# 미로 탈출 문제

# N x M 크기의 직사각형 형태의 미로에 갇혀있다.
# 미로에는 괴물이 있어 이를 피해 탈출해야 한다.
# 처음 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하여
# 한 번에 한 칸씩 이동할 수 있다.
# 괴물이 있는 부분은 0, 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출 할 수 있는 형태로 제시된다.
# 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력조건
# 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다.
# 각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
# 시작칸과 마지막 칸은 항상 1이다.
# (1, 1)부터 출발

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 예시
# 10

# 문제 해결 아이디어
# BFS 수행
# 근처 노드를 탐색하여 1일 때 수행

#####################################
# 풀이

from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우) (방향벡터)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 구현
def bfs(x, y):
    # 큐(Queue)를 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0,0))
