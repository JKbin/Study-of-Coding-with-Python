import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())

q = []
for i in range(n):
    q.append(int(input().rstrip()))
    
result = 0

heapq.heapify(q)

while len(q)!=1:
    
    one = heapq.heappop(q)
    two = heapq.heappop(q)
    
    sum_value = one + two
    result += sum_value
    heapq.heappush(q,sum_value)

print(result)

    
    

    

