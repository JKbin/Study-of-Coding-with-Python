from collections import deque
import sys

input = sys.stdin.readline

n,m,k = map(int,input().rstrip().split())
graph = [[5]*n for i in range(n)]
yangboon = []
for _ in range(n):
    yangboon.append(list(map(int,input().rstrip().split())))

trees = [[deque() for _ in range(n)] for _ in range(n)]         # 속도 때문에 deque 사용
for _ in range(m):
    x,y,age = map(int,input().rstrip().split())
    trees[x-1][y-1].append(age)
    
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]



def spring_summer():
    # 봄
    for i in range(n):
        for j in range(n):
            tree_cnt = len(trees[i][j])                 # 각 i,j의 deque의 길이만큼 수행
            for k in range(tree_cnt):
                if graph[i][j] >= trees[i][j][k]:
                    graph[i][j] -= trees[i][j][k]       # 양분먹기
                    trees[i][j][k] += 1                 # 나이추가
                else:
                    # 여름
                    # 죽어야하는 나무들(뒤에 있는 나무들 전부다)
                    for s in range(k,tree_cnt):
                        graph[i][j] += trees[i][j].pop() // 2
                    break
                
                    
                    
                
            
def fall_winter():
    # 가을
    for i in range(n):
        for j in range(n):
            cnt = len(trees[i][j])
            for k in range(cnt):
                if trees[i][j][k] % 5 == 0:
                    
                    for z in range(8):
                        nx = i + dx[z]
                        ny = j + dy[z]
                        
                        if 0<=nx<n and 0<=ny<n:
                            trees[nx][ny].appendleft(1)         # 속도 때문에 appendleft 사용
    # 겨울
    for i in range(n):
        for j in range(n):
            graph[i][j] += yangboon[i][j]
        
            
            
                            
            
                    

for _ in range(k):
    spring_summer()
    fall_winter()
    
res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[i][j])
        
print(res)


    
    



    

    