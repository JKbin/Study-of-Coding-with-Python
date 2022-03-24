import sys

input = sys.stdin.readline

# n : 심사대수, m : 학생수
n,m = map(int,input().rstrip().split())
arr = []

for i in range(n):
    arr.append(int(input().rstrip()))
    

start = min(arr)
end = max(arr) * (m)

ans = 0
while start <= end:
    mid = (start+end) // 2
    
    total = 0
    for i in arr:
        total += mid // i
    
    if total >= m:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
        
        
        
        
print(ans)

        
        
    


        
