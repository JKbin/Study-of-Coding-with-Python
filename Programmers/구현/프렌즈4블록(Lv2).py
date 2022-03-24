m,n = 4,5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]	

import copy



def solution(m,n,board):
    global cnt
    cnt = 0
    graph = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            graph[i][j] = board[i][j]
    graph2 = copy.deepcopy(graph)
    
    while True:
        check = bomb(graph,graph2,m,n)
        if not check:
            break
        count(graph2,m,n)
        graph2 = down(graph2,m,n)
        graph = copy.deepcopy(graph2)
        
    return cnt


# 블록 터뜨리기
def bomb(graph,graph2,m,n):
    
    check = 0
    for i in range(m-1):
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1] and graph[i][j].isalpha():        # 윗줄 2개가 같고
                if (graph[i][j] == graph[i+1][j]) and (graph[i][j+1] == graph[i+1][j+1]):        # 아랫줄 2개가 같으면
                    graph2[i][j] = '1'
                    graph2[i][j+1] = '1'
                    graph2[i+1][j] = '1'
                    graph2[i+1][j+1] = '1'
                    check += 1
    
    if check > 0:
        return True
    return False

# 터뜨린 블럭 카운트하기                    
def count(graph2,m,n):
    global cnt
    for i in range(m):
        for j in range(n):
            if graph2[i][j] == '1':
                cnt += 1
    return cnt
    
    
                    
# 블럭 밑으로 내리기
def down(graph2,m,n):
    
    while True:
        check = 0
        for i in range(m-1):
            for j in range(n):
            
                if (graph2[i+1][j] == '1' or graph2[i+1][j]=='0') and not graph2[i][j].isdigit():
                    graph2[i+1][j] = graph2[i][j]
                    graph2[i][j] = '0'
                    check += 1
        if check == 0:
            break
    
    for i in range(m):
        for j in range(n):
            if graph2[i][j] == '1':
                graph2[i][j] = '0'
    return graph2


print(solution(m,n,board))
