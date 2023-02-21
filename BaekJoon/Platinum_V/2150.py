# 타잔 알고리즘
# 그래프 상의 강한 결합 요소를 찾는 알고리즘

# 백준 2150


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def scc(graph, V):
    finished = [False] * (V+1)
    label = [0] # 누적 라벨 : 노드를 한 번 방문할 때마다 1씩 증가
    labels = [0] * (V+1)
    result, s = [], []
    
    def _scc(u):
        label[0] += 1
        parent = labels[u] = label[0]       # 자기 자신이 부모노드로 가정
        s.append(u)
        
        for v in graph[u]:
            if not labels[v]:
                # 아직 방문 x
                parent = min(parent, _scc(v))
            elif not finished[v]:
                # 방문은 했으나 SCC 처리가 안된 노드 = 사이클
                parent = min(parent, labels[v])
        
        if parent == labels[u]:
            # 자기 자신이 사이클 중 가장 먼저 탐색되었다? == 내가 루트노드이다.
            
            scc_set = []
            while s:
                p = s.pop()
                scc_set.append(p)
                finished[p] = True
                if u == p:
                    break
            result.append(scc_set)
        return parent


    for e in range(1, V+1):
        if not labels[e]:
            _scc(e)
    return result
            
    
    


V, E = map(int,input().rstrip().split())
graph = [[]for _ in range(V+1)]

for _ in range(E):
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    
answer = scc(graph, V)

for i in answer:
    i.sort()

print(len(answer))
answer.sort(key=lambda x:x[0])

for i in answer:
    print(' '.join(map(str, i))+' -1')
    
    
    
        


    

