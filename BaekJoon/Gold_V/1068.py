from sys import stdin


n = int(stdin.readline().rstrip())
graph = list(map(int,stdin.readline().rstrip().split()))
k = int(stdin.readline().rstrip())

# n = 5
# graph = [-1, 0, 0, 1, 1]
# k = 2

# graph = 부모노드의 집합
# k : 삭제할 부모노드

def dfs(k,graph):
    graph[k] = -2
    for i in range(len(graph)):
        # 부모노드가 k인것을 -2로 만들기
        if k == graph[i]:
            dfs(i,graph)
            
            
dfs(k,graph)
count = 0



for i in range(len(graph)):
    # 부모노드가 삭제가 안되었고, i가 graph에 없는 경우 count += 1
    if graph[i] != -2 and i not in graph:
        count += 1
        
print(count)
        
                




             
             