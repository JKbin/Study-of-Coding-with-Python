from copy import deepcopy
import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

# 우좌상하
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# cctv 번호별로 감시할 수 있는 방향 정의
cctvs_dir = {1:[[0],[1],[2],[3]],2:[[0,1],[2,3]],3:[[0,2],[0,3],[3,1],[1,2]],4:[[1,2,0],[2,0,3],[0,1,3],[2,1,3]],5:[[0,1,2,3]]}

cctvs = []
for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctvs.append([i,j,graph[i][j]])

res = sys.maxsize     # 사각지대의 최소크기

def graph_sum(graph):
    tmp = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                tmp += 1
    return tmp
            

# 감시
def fill(graph,dirs,x,y):
    for i in dirs:
        nx = x 
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
                elif graph[nx][ny] == 6:
                    break
            else:
                break
            
                    
# index를 깊이 삼아 재귀함수 수행
def dfs(graph,index):
    global res
    grp = deepcopy(graph)
    
    if index == len(cctvs):
        res = min(res,graph_sum(graph))
        return
    
    x,y,cctv_num = cctvs[index] 
    possible_dir = cctvs_dir[cctv_num]          # cctv번호가 감시할 수 있는 배열 선언
    
    for i in possible_dir:
        fill(grp,i,x,y)
        dfs(grp,index+1)
        grp = deepcopy(graph)
        
        
        
        
        

dfs(graph,0)
print(res)


    


    
    
        
        
        
    
    










