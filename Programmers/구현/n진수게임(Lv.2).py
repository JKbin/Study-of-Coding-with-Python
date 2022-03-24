import string
n,t,m,p = 2,4,2,1


def convert(num, base) :
    tmp = string.digits+string.ascii_uppercase
    
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
    
  

def solution(n,t,m,p):
    
    result = ''
    temp = ''
    
        
    for i in range(m*t):
        a = convert(i,n)
        temp += str(a)
        
    for i in range(p-1,len(temp),m):
        if len(result) != t:
            result += temp[i]
        
            
    return result


print(solution(n,t,m,p))
