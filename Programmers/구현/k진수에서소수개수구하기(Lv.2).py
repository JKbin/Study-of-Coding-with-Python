import math
import string

n = 437674
k = 3
# 소수 판별 함수
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x)+1)):
        
        if x % i == 0:
            return False
    return True

# k진수로 변환
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]



def solution(n,k):
    a = convert(n,k)
    temp2 = []

    b = a.split('0')

    for i in b:
        if len(i) > 0:
            if int(i) > 1 and is_prime_number(int(i)):
                temp2.append(i)
                
    return len(temp2)


print(solution(n,k))
