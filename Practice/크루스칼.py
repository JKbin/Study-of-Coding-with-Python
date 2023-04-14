# 신장트리 : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프(MST)
# 크루스칼 알고리즘 : 가장 적은 비용으로 모든 노드를 연결할 수 있을 때
# 시간 복잡도 : 간선의 개수가 E개일 때, O(ElogE)의 시간 복잡도를 가진다.

# BOJ 1922

import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

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
    
edges = []
result = 0

parent = [0] * (n+1)                
for i in range(1, n+1):             # 부모 자기 자신으로 초기화
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().rstrip().split())
    edges.append((cost, a, b))         # 비용 순으로 정렬 할거니깐 이렇게 집어넣기
    
# 비용순으로 정렬
edges.sort()        
    
    
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

    


        
    



    