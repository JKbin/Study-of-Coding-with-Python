def rotate(a):
    n = len(a)      # 행 
    m = len(a[0])   # 열
    result = [[0]*n for i in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

a = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate(a))


    
    
    