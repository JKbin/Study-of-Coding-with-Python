# DFS

import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input().rstrip())    

graph = [[]for i in range(n+1)]

table = {}
now = 2
# 그래프 및 테이블 정의
for i in range(n-1):
    ani, mari, conn = input().rstrip().split()
    
    mari = int(mari)
    conn = int(conn)
    
    graph[conn].append(now)
    table[now] = [ani, mari]
    now += 1
    
    
# 늑대면면 늑대도 빼줘야함
# 양이면 그냥 더하기
def dfs(now_num):
    result = 0
    
    for i in graph[now_num]:
        result += dfs(i)
        
    if now_num == 1:
        return result
    
    animal = table[now_num][0] 
    mari = table[now_num][1]
    
    if animal == 'W':
        
        if result > mari:
            table[now_num][1] = 0
            result -= mari
        elif result < mari:
            table[now_num][1] = mari - result
            result = 0
    else:
        result += mari
    return result


print(dfs(1))
