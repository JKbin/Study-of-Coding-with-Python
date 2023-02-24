import sys
# 부분합 계산, 투포인터

input = sys.stdin.readline

n,S = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

_sum = arr[0]
i,j = 0,0
ans = sys.maxsize

while True:
    if _sum >= S:
        _sum -= arr[i]
        ans = min(ans, j - i + 1)
        i += 1
    else:
        j += 1
        if j == n:
            break
        _sum += arr[j]
        

print(ans) if ans != sys.maxsize else print(0)

        
    
        
        
    
    