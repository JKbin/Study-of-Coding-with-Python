
import sys

input = sys.stdin.readline

n = int(input().rstrip())
table = {}
for i in range(n**2):
    num = list(map(int,input().rstrip().split()))
    key = num[0]
    value = num[1:]
    table[key] = value

# n = 3
# table = {4: [2, 5, 1, 7], 3: [1, 9, 4, 5], 9: [8, 1, 2, 3], 8: [1, 9, 3, 4], 7: [2, 3, 4, 8], 1: [9, 2, 5, 7], 6: [5, 2, 3, 4], 5: [1, 9, 2, 8], 2: [9, 3, 1, 4]}

numbers = list(table.keys())
graph = [[0]*(n)for i in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

res = 0


while numbers:
    num = numbers.pop(0)
    
    # 인접한 칸 중 비어있는 칸 구하기 + 인접한 칸에 좋아하는 학생 수 구하기
    tmp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                blankcnt = 0
                likecnt= 0
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == 0:          # 빈 칸 구하기
                            blankcnt += 1
                        if graph[nx][ny] in table[num]: # 좋아하는 학생 수 구하기
                            likecnt += 1
                tmp.append((i,j,blankcnt,likecnt))
    # 정렬순서 : likecnt, blankcnt, 행, 열
    tmp.sort(key=lambda x:(x[3],x[2],-x[0],-x[1]),reverse=True)
    temp = tmp[0]
    graph[temp[0]][temp[1]] = num
    

# 만족도 구하기
for i in range(n):
    for j in range(n):
        a = graph[i][j]
        t_cnt = 0
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] in table[a]:
                    t_cnt += 1
                    
        if t_cnt == 1:
            res += 1
        elif t_cnt == 2:
            res += 10
        elif t_cnt == 3:
            res += 100
        elif t_cnt == 4:
            res += 1000
            
print(res)

            
            

