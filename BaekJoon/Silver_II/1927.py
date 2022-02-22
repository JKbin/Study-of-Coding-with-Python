import heapq
import sys

n = int(sys.stdin.readline().rstrip())

hq = []

for i in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(hq,(x,-x))
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[0])


        










