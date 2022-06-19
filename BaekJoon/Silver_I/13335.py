import sys

input = sys.stdin.readline

n,w,l = map(int,input().rstrip().split())        

# n : 트럭의 수
# w : 다리의 길이
# l : 다리의 최대하중

arr = list(map(int,input().rstrip().split()))

bridge = [0 for i in range(w)]
ans = 0

while bridge:
    bridge.pop(0)
    ans += 1
    
    if arr:
        if sum(bridge) + arr[0] <= l:
            bridge.append(arr.pop(0))
        else:
            bridge.append(0)
            
        
print(ans)
        