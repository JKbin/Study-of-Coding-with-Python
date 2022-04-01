# 시간 복잡도 
# n^n : 중복이 가능, n = 8 까지 가능
# n ! : 중복이 불가능, n = 10 까지 가능

# 백준 15649

import sys
input = sys.stdin.readline



n,m = map(int,input().rstrip().split())

res = []
chk = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str,res)))
        
    for i in range(1,n+1):
        if chk[i] == False:
            chk[i] = True
            res.append(i)
            recur(num+1)
            chk[i] = False
            res.pop()



recur(0)