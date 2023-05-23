# 경로의 최댓값 구하기 문제 (dp)
# 왼쪽에서 오는 경로, 오른쪽에서 오는 경로 각 각 구해서 최대값 구하기

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))


# 첫 번째 줄 초기화
for i in range(1, m):
    graph[0][i] += graph[0][i-1] 

# 두 번째 줄 부터 왼쪽에서 오는 경우, 오른쪽에서 오는 경우 2가지로 나누어서 계산
for i in range(1, n):
    left_to_right = graph[i][:]
    right_to_left = graph[i][:]
    

    # 1. 왼쪽에서 오른쪽으로 진행하는 경우
    for j in range(m):
        # j == 0인 경우는 위쪽에서 오는 경로 1가지 뿐
        if j == 0:
            left_to_right[j] += graph[i-1][j]
        else:
            left_to_right[j] += max(left_to_right[j-1], graph[i-1][j])
    
    #2. 오른쪽에서 왼쪽으로 진행하는 경우
    for j in range(m-1, -1, -1):
        # j == m-1 (맨 오른쪽인 경우)는 위쪽에서 오는 경로 1가지 뿐
        if j == m-1:
            right_to_left[j] += graph[i-1][j]
        else:
            right_to_left[j] += max(right_to_left[j+1], graph[i-1][j])
            
    # 3. left_to_right, right_to_left 두 개의 배열을 비교해서 더 큰 값 graph에 업데이트하기
    for j in range(m):
        graph[i][j] = max(left_to_right[j], right_to_left[j])
        

print(graph[-1][-1])

    


    

    
    