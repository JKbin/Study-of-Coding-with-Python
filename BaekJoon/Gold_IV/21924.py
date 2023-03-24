# MST
# 전체 비용 - 최소 비용
# 사이클 존재 여부

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
    
n, m = map(int, input().rstrip().split())    

total_price = 0

edges = []
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    edges.append([c,a,b])
    total_price += c
    
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i
    
edges.sort()

price = 0
for edge in edges:
    c, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        price += c
        
cycle = True
first = parent[1]  
for i in parent[1:]:
    if parent[i] != first:
        cycle = False
        break

if not cycle:
    print(-1)
else:
    print(total_price - price)
