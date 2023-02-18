import sys
input = sys.stdin.readline

# 시간 복잡도
# V : 노드의 개수 
# M : find 연산의 개수
# 예를 들어 노드의 개수가 1,000개고 union 및 find의 연산이 100만 번 수행 된다고 하자.
# 대략 V + MlogV 의 시간 복잡도를 갖는다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
        
v,e = map(int,input().split())
parent = [0] * (v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i


# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
    
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블: ',end=' ')
for i in range(1,v+1):
    print(parent[i],end=' ')
    
    
    
    