# 우선순위 큐 (이중)
# 최소힙, 최대힙, 구분자 v 변수 설정


import sys, heapq

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    v = [0] * (n)       # 0이면 존재x, 1이면 존재0
    
    minq = []
    maxq = []
    
    for idx in range(n):
        
        
        alpha, num = input().rstrip().split()
        num = int(num)
        
        if alpha == 'I':
            heapq.heappush(minq, (num, idx))
            heapq.heappush(maxq, ((num*-1), idx))
            v[idx] = 1                              # idx값 존재
            
        elif alpha == 'D':
            if num == 1:                            # 최댓값 삭제
                
                if maxq:                            # 최소힙과 동기화
                    while maxq:
                        if v[maxq[0][1]] == 0:
                            heapq.heappop(maxq)
                        else:
                            break
                    if maxq:
                        flag = maxq[0][1]
                        v[flag] = 0
                        heapq.heappop(maxq)
                
            elif num == -1:                         # 최솟값 삭제
                if minq:
                    while minq:                     # 최대힙과 동기화
                        if v[minq[0][1]] == 0:
                            heapq.heappop(minq)
                        else:
                            break
                    if minq:
                        flag = minq[0][1]
                        v[flag] = 0
                        heapq.heappop(minq)
        
    # 마지막으로 최소힙, 최대힙 각각 동기화 시키기
    answer = []
    while minq:
        if v[minq[0][1]] == 0:
            heapq.heappop(minq)
        else:
            break
    while maxq:
        if v[maxq[0][1]] == 0:
            heapq.heappop(maxq)
        else:
            break
            
    if minq:
        print((maxq[0][0]*-1), minq[0][0])
    else:
        print('EMPTY')
         
    
        
        
        
    
    
