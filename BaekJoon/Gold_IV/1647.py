import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
parent = [0] * (n+1)

result = 0      # 최종 비용
last = 0        # MST에 포함되는 간선 중 가장 비용이 큰 간선

# parent 초기화
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph.append((c,a,b))

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


graph.sort()


for i in graph:
    cost, a, b = i
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost


#print(parent)
print(result-last)
#print(last)



    
    
    

