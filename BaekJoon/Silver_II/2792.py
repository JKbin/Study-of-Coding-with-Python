import sys,math

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
arr = []
for _ in range(m):
    arr.append(int(input().rstrip()))
    
start = 1
end = max(arr)
ans = 0

while start <= end:
    
    mid = (start+end) // 2
    
    cnt = 0
    for i in arr:
        cnt += math.ceil(i / mid)
    
    if cnt > n:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
        
        
print(ans)

        
        
    