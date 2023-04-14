# 이분 매칭의 전형적인 문제
# 백준 2188

import sys
input = sys.stdin.readline

def dfs(cow_number):
    if visited[cow_number]:
        return False
    visited[cow_number] = True
    
    for i in cow[cow_number]:
        if not cattle_shed[i] or dfs(cattle_shed[i]):
            cattle_shed[i] = cow_number
            return True
        
    return False

n, m = map(int, input().rstrip().split())
cow = [[]for _ in range(n+1)]
cattle_shed = [0 for _ in range(m+1)]

for i in range(1, n+1):
    array = list(map(int, input().rstrip().split()))
    for j in array[1:]:
        cow[i].append(j)

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(i)

print(cattle_shed)
