# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 방향 그래프의 모든 노드를 '방향성에 거슬리지 않도록 순서대로 나열하는 것'
# 시간 복잡도 : O(V+E)

from collections import deque
import sys
input = sys.stdin.readline
# 노드의 개수와 간선 입력 받기
v,e = map(int,input().rstrip().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 간선 정보 입력 받기
for i in range(e):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1
    

# 위상 정렬 함수
def toplogy_sort():
    result = []
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
            
    
    # 큐가 빌 때까지 반복
    while q:
        
        now = q.popleft()
        result.append(now)
        
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입사추가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                
    for i in result:
        print(i,end= ' ')

toplogy_sort()


                

        
