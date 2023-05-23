# 그래프 깊이 탐색

import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input().rstrip())
graph = dict()
find_root_node = [0] * (n+1)

for _ in range(n):
    node, left, right = map(int, input().rstrip().split())  
    if left == -1:
        left = None
    if right == -1:
        right = None
    graph[node] = [left, right]
    
    find_root_node[node] += 1
    if left != None:
        find_root_node[left] += 1
    if right != None:
        find_root_node[right] += 1
    
# 좌표를 담을 변수
table = dict()
for j in range(1, n+1):
    table[j] = [-1, -1]
    
# y좌표 정하기
def depth(now, d):
    table[now][1] = d
    z = graph[now]
    left, right = z[0], z[1]
    if left != None:
        depth(left, d+1)
    if right != None:
        depth(right, d+1)
        
# x좌표 정하기
def width(now):
    global idx
    
    z = graph[now]
    left, right = z[0], z[1]
    
    # 왼쪽 자식 노드부터 탐색
    if left != None:
        width(left)
    elif left == None:
        table[now][0] = idx
        idx += 1
        if right != None:
            width(right)
    
    if table[now][0] == -1:
        table[now][0] = idx
        idx += 1
        if right != None:
            width(right)
    
rootNode = -1
# 루트 노드 찾기
# 1 ~ n+1까지 언급된 것이 1이면 rootNode
for i in range(1, n+1):
    if find_root_node[i] == 1:
        rootNode = i
        break
    
# y좌표 찾기 (level)
depth(rootNode, 1)

# x좌표 찾기    
idx = 1
width(rootNode)

# level마다 너비 계산하기
level = defaultdict(list)
for node in table:
    c = table[node]
    x, y = c[0], c[1]
    level[y].append(x)
    
result = defaultdict(int)
for l in level:
    result[l] = (max(level[l]) - min(level[l]) + 1)
    
# 너비가 큰 쪽으로, level이 작은 순으로 정렬
result = list(result.items())
result.sort(key=lambda x:(-x[1], x[0]))

print(*result[0], end=' ')

