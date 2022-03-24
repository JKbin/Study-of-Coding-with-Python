from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input().rstrip())
#n = 5

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
for i in range(n):
    graph.append(list(map(str,input().rstrip().split())))
# graph = [['X', 'S', 'X', 'X', 'T'], ['T', 'X', 'S', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 
# 'T', 'X', 'X', 'X'], ['X', 'X', 'T', 'X', 'X']]

def check(x,y,direction):
    # 상
    if direction == 0:
        while x >= 0:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            x -= 1
    # 하   
    elif direction == 1:
        while x < n:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            x += 1
    # 좌
    elif direction == 2:
        while y >= 0:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            y -= 1
    
    # 우
    elif direction == 3:
        while y < n:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            y += 1
    return False
        
        
def bfs():
    # 3. 선생님에 대해서 상,하,좌,우 검사하기
    q = deque(teachers)
    
    while q:
        
        x,y = q.popleft()
        
        for i in range(4):
            
            if check(x,y,i):
                return True
    return False
                
    
            
            
        


teachers = []
objects = []

# 1. 선생님의 위치와 빈 곳의 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            objects.append((i,j))
        elif graph[i][j] == 'T':
            teachers.append((i,j))
            
flag = False
# 2. 3개의 장애물 설치 구역에 대해서
for A,B,C in combinations(objects,3):
    # 장애물 설치
    graph[A[0]][A[1]] = 'O'
    graph[B[0]][B[1]] = 'O'
    graph[C[0]][C[1]] = 'O'
    
    
    if not bfs():
        flag = True
        break
    
    graph[A[0]][A[1]] = 'X'
    graph[B[0]][B[1]] = 'X'
    graph[C[0]][C[1]] = 'X'
    
    

if flag:
    print('YES')
else:
    print('NO')
    