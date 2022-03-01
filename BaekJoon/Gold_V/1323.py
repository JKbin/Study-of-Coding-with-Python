from sys import stdin


n,k = map(int,stdin.readline().rstrip().split())
seta = set()
temp = n
cnt = 0


while True:
    
    
    a,temp = divmod(int(temp),k)
    cnt += 1
    
    if temp == 0:
        print(cnt)
        break
    
    else:
        temp = str(temp) + str(n)
        
        if temp in seta:
            print(-1)
            break
        
        else:
            seta.add(temp)
            
            
    
    
    
    
        
        
    
    
    
    
    
        
        




