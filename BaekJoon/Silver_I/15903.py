import heapq
import sys

input = sys.stdin.readline


n,m = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))

    
    

heapq.heapify(arr)

while m > 0:
    m -= 1
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    
    sum_num = x + y
    heapq.heappush(arr,sum_num)
    heapq.heappush(arr,sum_num)
    
    
print(sum(arr))

    