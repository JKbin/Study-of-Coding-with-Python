import heapq

nums = [4,1,6,3,8,5]

heap = []

# 최대 힙 구하기
# for i in nums:
#     heapq.heappush(heap,(-i,i))
# while heap:
#     print(heapq.heappop(heap)[1])
    
    
# 최소 힙 구하기
for i in nums:
    heapq.heappush(heap,i)
    
while heap:
    print(heapq.heappop(heap))
    
    

    

