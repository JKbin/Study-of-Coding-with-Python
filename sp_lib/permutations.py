def permutation(arr, n):    
    result = []    
    if n == 0:        
        return [[]]        
    for i in range(len(arr)):        
        elem = arr[i]        
        for rest in permutation(arr[:i] + arr[i+1:], n - 1):            
            result.append([elem] + rest)    
    return result    


print(permutation([1,2,3,4,5], 3))