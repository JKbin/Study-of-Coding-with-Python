n,m = 4,6           # n : 떡의 개수, m : 필요한 떡의 길이
arr = [19,15,10,17] # arr : 떡의 길이


end = max(arr)
start = 0
result = 0


while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in arr:
        if x > mid:
            total += (x - mid)
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)
    
    



    
        
        
    
    
