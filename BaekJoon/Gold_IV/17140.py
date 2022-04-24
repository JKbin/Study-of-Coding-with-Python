import sys
from typing import Counter

input = sys.stdin.readline


r,c,k = map(int,input().rstrip().split())
#r,c,k = 3,3,3

graph = []
#graph = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

for _ in range(3):
    graph.append(list(map(int,input().rstrip().split())))
    

# R연산
def R_fun(graph):
    change_graph = [[]for i in range(len(graph))]
    max_length = 0
    
    if len(graph) > 100:
        return graph
    
    for i in range(len(graph)):
        temp = []
        a = Counter(graph[i])
        for j in Counter(graph[i]).keys():
            if j != 0:
                temp.append((j,a[j]))
        temp.sort(key=lambda x:(x[1],x[0]))
        for k in temp:
            change_graph[i].extend(k)
            max_length = max(max_length,len(change_graph[i]))
            
    for i in range(len(change_graph)):
        if len(change_graph[i]) < max_length:
            for j in range(max_length-len(change_graph[i])):
                change_graph[i].append(0)
                
    return change_graph
                
                
            
# C연산
def C_fun(graph):
    
    if len(graph) > 100:
        return graph
    else:
        change_graph = list(zip(*graph))
        change_graph = R_fun(change_graph)
        change_graph = list(zip(*change_graph))
        return change_graph
    
    
time = 0
check = False

while time <= 100:
    n = len(graph)      # 행의 개수
    m = len(graph[0])   # 열의 개수
    
    try:
        if graph[r-1][c-1] == k:
            check = True
            print(time)
            break
    except:
        pass
    
    if n >= m:
        # R연산
        graph = R_fun(graph)
    else:
        graph = C_fun(graph)
        pass
    time += 1
if not check:
    print(-1)
    
    
    
        
    
    
    