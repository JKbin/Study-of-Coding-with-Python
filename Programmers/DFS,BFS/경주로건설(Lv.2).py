from collections import deque
import sys

board = [[0,0,0],[0,0,0],[0,0,0]]	
def solution(board):
    
    def bfs(start):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]     # i = 상(0),하(1),좌(2),우(3)
        n = len(board)
        visited = [[sys.maxsize]*(n)for i in range(n)]
        visited[0][0] = 0
        
        # start = x좌표,y좌표,비용,방향
        q = deque([start])
        while q:
            x,y,c,d = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                    # 진행방향에 따른 비용 추가
                    if i == d:
                        nc = c + 100
                    else:
                        nc = c + 600
                        
                    if nc < visited[nx][ny]:
                        visited[nx][ny] = nc
                        q.append([nx,ny,nc,i])
        return visited[-1][-1]
    
    return min(bfs((0,0,0,1)),bfs((0,0,0,3)))           # 처음에 출발은 동쪽 or 남쪽만 가능
                        
                    
    

print(solution(board))


        
        
    