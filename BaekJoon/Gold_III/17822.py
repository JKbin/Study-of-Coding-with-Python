from collections import deque
import sys
input = sys.stdin.readline

N,M,T = map(int,input().rstrip().split())
graph = [[0]*N]
query = []
for _ in range(N):
    graph.append(deque(map(int,input().rstrip().split())))
for _ in range(T):
    query.append(list(map(int,input().rstrip().split())))


def rotate(x,graph,d,k):
    if d == 0:                  # 시계방향
        graph[x].rotate(k)
    else:                       # 반시계방향
        graph[x].rotate(-k)
        
    
# 인접한 수 check
def check(graph):
    visited = [[False]*(M) for i in range(N+1)]
    global chk
    
    # 가로방향 check
    for i in range(1,N+1):
        for j in range(M-1):
            if graph[i][j] != '#':
                if graph[i][j] == graph[i][j+1]:
                    visited[i][j] = True
                    visited[i][j+1] = True
                    chk = True
    # 맨 앞과 맨 뒤 체크
    for i in range(1,N+1):
        if graph[i][0] != '#':
            if graph[i][0] == graph[i][-1]:
                visited[i][0] = True
                visited[i][-1] = True
                chk = True
    # 세로방향 check
    for i in range(1,N):
        for j in range(M):
            if graph[i][j] != '#':
                if graph[i][j] == graph[i+1][j]:
                    visited[i][j] = True
                    visited[i+1][j] = True
                    chk = True
                    
    # 인접한 수 없애기            
    for i in range(1,N+1):
        for j in range(M):
            if visited[i][j] == True:
                graph[i][j] = '#'
                
                
                
                
        
                    
# 평균구하기     
def average(graph):
    tmp_sum = 0
    cnt = 0
    for i in range(1,N+1):
        for j in range(M):
            if graph[i][j] != '#':
                tmp_sum += graph[i][j]
                cnt += 1
    
    if cnt > 0:         # graph가 모두 '#'인 경우 dividezero exception 발생    
        avg = tmp_sum / cnt
        for i in range(1,N+1):
            for j in range(M):
                if graph[i][j] != '#':
                    if graph[i][j] > avg:
                        graph[i][j] -= 1
                    elif graph[i][j] < avg:
                        graph[i][j] += 1
                    
# 총합 구하기 
def sum_graph(graph):
    tmp_sum = 0
    for i in range(1,N+1):
        for j in range(M):
            if graph[i][j] != '#':
                tmp_sum += graph[i][j]               
    return tmp_sum
                    
result = 0

for i in range(T):
    x,d,k = query[i]
    chk = False
    
    for j in range(x,N+1,x):
        rotate(j,graph,d,k)
    
    check(graph)
    
    if chk:
        result = result + sum_graph(graph) - result
        
    if not chk:
        average(graph)
        result = result + sum_graph(graph) - result
        
print(result)

        
        
        
    
                 
    
    
        
        
        
        
        
        
        
    
        