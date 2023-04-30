# MST , 크루스칼 알고리즘
# 좌표 거리 구해서 그래프 새로 만들기

import sys, math
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 좌표를 담을 임시 변수
t = dict()      
for i in range(1, n+1):
    a, b = map(int, input().rstrip().split())
    t[i] = [a, b]
    
# 이미 연결되어 있는 노드들의 정보를 담는 변수
con = []        
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    con.append([a, b])

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:   
        parent[a] = b
    
# 간선의 정보를 담는 변수
graph = [[]for i in range(n+1)]

# parent 변수 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# 좌표로 받은 것들의 모든 거리 구해서 graph에 넣기 (양방향 간선)
for i in combinations(list(t.keys()), 2):
    x, y = i[0], i[1]
    
    x_1, y_1 = t[x][0], t[x][1]
    x_2, y_2 = t[y][0], t[y][1]
    
    dist = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    
    graph[x].append((y, dist))
    graph[y].append((x, dist))
    
# 이미 연결되어 있는 정보들 union
for a, b in con:
    union_parent(parent, a, b)

# (cost, start, next) 순으로 edges 변수에 집어 넣기
edges = []
for i in range(1, n+1):
    for next_node, cost in graph[i]:
        edges.append((cost, i, next_node))

# 비용순으로 정렬
edges.sort()
res = 0

# 최소로 연결되었을 때 비용 구하기
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(f'{res:.2f}')


        
    

        


    
    

    
    

    

    