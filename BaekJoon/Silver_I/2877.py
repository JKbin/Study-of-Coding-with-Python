
# '0' : '4' , '1' : '7'
# n + 1 -> 2진수로 변환 -> 맨앞자리빼고 구하기

from sys import stdin


n = int(stdin.readline().rstrip())

def fun(n):
    ans = ''
    n += 1
    
    n = bin(n).split('0b')[1]
    n = n[1:]
    
    for i in n:
        if i == '0':
            ans += '4'
        else:
            ans += '7'
    
    return ans
            
print(fun(n))
        
        
    
    
    