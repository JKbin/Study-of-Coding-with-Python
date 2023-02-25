import sys

# 서로소 판별, 사이클이 이루어지는지 문제

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i 

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
    

for i in range(1,n+1):
    link = list(map(int, input().rstrip().split()))
    for j in range(len(link)):
        if link[j] == 1:
            union_parent(parent, i, j+1)

path = list(map(int, input().rstrip().split()))
            

start = parent[path[0]]

for i in range(m):
    if parent[path[i]] != start:
        print('NO')
        break
else:
    print('YES')
    
