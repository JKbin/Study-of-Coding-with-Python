from itertools import combinations
import  sys
from string import ascii_lowercase

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
#n,m = 4,6
arr = list(map(str,input().rstrip().split()))
#arr = ['a','t','c','i','s','w']

arr.sort()                  # 입력 받은 배열 정렬
a = set(list(ascii_lowercase))
mo = ['a','e','i','o','u']  # 모음
ja = list(a-set(mo))        # 자음
ja.sort()

res = []
for i in combinations(arr,n):
    b = ''.join(i)
    
    mo_chk = 0
    ja_chk = 0
    for j in b:
        if j in mo:
            mo_chk += 1             # 모음 개수 체크
        elif j in ja:
            ja_chk += 1             # 자음 개수 체크
        
    if ja_chk >= 2 and mo_chk >= 1:
        res.append(b)


for i in res:
    print(i)

            
        
        
        





        





