#n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5
#n, m, x, y, r, c, k = 2, 2, 1, 1, 2, 2, 2
n, m, x, y, r, c, k = 3, 3, 1, 2, 3, 3, 4,


#dx = [-1,1,0,0]
#dy = [0,0,-1,1]
# 상(u),하(d),좌(l),우(r)

dir = [ ('d',1,0), ('l',0,-1), ('r',0,1), ('u',-1,0) ]

from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    # n : row
    # m : col
    # x : start x
    # y : start y
    # r : end x
    # c : end y
        
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    
    q = deque()
    q.append( (x,y,'',0) )
    
    
    while q:
        cur_x, cur_y, cur_str, cur_cnt = q.popleft()
        
        if cur_cnt == k and (cur_x, cur_y) == (r, c):
            return cur_str
        
        for i in range(4):
            nx = cur_x + dir[i][1]
            ny = cur_y + dir[i][2]
            nstr = cur_str + dir[i][0]
            
            if 0<=nx<n and 0<=ny<m and cur_cnt <= k:
                if abs(nx-r) + abs(ny-c) + cur_cnt + 1 <= k:         # 남은 거리 미리 계산
                    q.append((nx,ny,nstr,cur_cnt+1))                
                    # d -> l -> r -> u 가 사전 순이기 때문에 앞이 ok 면 뒤는 필요 없음
                    break                                           
                
                
    return "impossible"
                
    
                
    
    
    
print(solution(n, m, x ,y, r, c, k))

    
    