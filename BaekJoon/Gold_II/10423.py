# MST, parent 조작

import sys

input = sys.stdin.readline

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
    

n,m,k = map(int, input().rstrip().split())
edges = []
baljeonso_list = list(map(int, input().rstrip().split()))
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    edges.append((c,a,b))
parent = [0] * (n+1)
    
result = 0

# 발전소이면 parent가 0, 아니면 자기 자신!!
for i in range(1,n+1):
    if i not in baljeonso_list:
        parent[i] = i

edges.sort()


for edge in edges:
    cost,a,b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)



    