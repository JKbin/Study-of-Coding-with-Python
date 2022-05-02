# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	

board = [[1,2,3],[4,5,6],[7,8,9]]	
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	


def solution(board, skill):
    answer = 0
    row = len(board)
    col = len(board[0])
    
    imos = [[0]*(col+1) for i in range(row+1)]
    
    # 각 가장자리마다 증가값 감소값 정하기
    for i in skill:
        if i[0] == 1:
            imos[i[1]][i[2]] += -i[5]
            imos[i[1]][i[4]+1] += i[5]
            imos[i[3]+1][i[2]] += i[5]
            imos[i[3]+1][i[4]+1] += -i[5]
        else:
            imos[i[1]][i[2]] += i[5]
            imos[i[1]][i[4]+1] += -i[5]
            imos[i[3]+1][i[2]] += -i[5]
            imos[i[3]+1][i[4]+1] += i[5]
            
    # 누적합 구하기
    for i in range(row):
        now = 0
        for j in range(col):
            now += imos[i][j]
            imos[i][j] = now
            
    for i in range(col):
        now = 0
        for j in range(row):
            now += imos[j][i]
            imos[j][i] = now
            
    # 최종으로 0보다 높은 구역 구하기   
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += imos[i][j]
            if board[i][j] > 0:
                answer += 1
                
    return answer
    



print(solution(board,skill))
