# 최소 스패닝 트리(MST)
# 전체 요금 - 최소 요금 = 절약한 요금

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
    
while True:
    n, m = map(int, input().rstrip().split())
    
    if n == 0 and m == 0:
        break
    
    edges = []
    parent = [0] * (n)
    total_price = 0
    
    for i in range(n):
        parent[i] = i
    
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        edges.append((c,a,b))
        total_price += c
    
    edges.sort()
    result = 0
    
    for edge in edges:
        cost,a,b = edge
        
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    print(total_price - result)
    
    
    
        

    
    
    


    
    
