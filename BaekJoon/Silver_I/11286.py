import heapq,sys
# 절댓값 힙
input = sys.stdin.readline

n = int(input().rstrip())

q = []

for _ in range(n):
    s = input().rstrip()
    
    if s != '0':
        heapq.heappush(q,(abs(int(s)),int(s)))
    elif s == '0':
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
            

        
        
        




