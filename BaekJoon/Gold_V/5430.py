import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())


for _ in range(n):
    query = input().rstrip()
    m = int(input().rstrip())
    arr = deque(input().rstrip()[1:-1].split(','))
    
    if m == 0:
        arr = []
    
    
    chk_R = 0
    
    for q in query:
        if q == 'R':
            chk_R += 1
        else:
            if len(arr) == 0:       # arr이 비어있는 경우
                print('error')
                break
            else:
                if chk_R % 2 == 0:      # R의 횟수가 짝수면 뒤집을 필요 없으므로 popleft()
                    arr.popleft()       
                else:                   # R의 횟수가 홀수면 뒤집어야하니깐 pop()
                    arr.pop()
    else:
        if chk_R % 2 == 0:
            print('['+','.join(arr)+']')
        else:
            arr.reverse()
            print('['+','.join(arr)+']')
            
            
    
                    
                    
            
        
        

    
    








