from copy import deepcopy
import  sys
from collections import deque

input = sys.stdin.readline

n = 4
q = []
for _ in range(4):
    q.append(deque(map(int,input().rstrip())))
query = []
k = int(input().rstrip())
for _ in range(k):
    a,b = map(int,input().rstrip().split())
    query.append([a,b])

# n = 4
# k = 2    
# q = [deque([1, 0, 1, 0, 1, 1, 1, 1]),deque([0, 1, 1, 1, 1, 1, 0, 1]),deque([1, 1, 0, 0, 1, 1, 1, 0]),deque([0, 0, 0, 0, 0, 0, 1, 0])]
# query = [[3, -1], [1, 1]]

# 시계방향 : 1, 반시계방향 : -1
table = {-1:1, 1:-1}

    # q, 비교대상, 기준
def left_check(q,i,num):         
    if q[num][6] == q[i][2]:
        return True        # 같으면 True
    return False            # 다르면 False

def right_check(q,i,num):
    if q[num][2] == q[i][6]:
        return True
    return False
        
    
        

for num,dir in query:
    num -= 1                
    
    tmp = deepcopy(q)
    tmp[num].rotate(dir)
    ldir = dir              # 왼쪽방향/오른쪽방향 따로 변수에 지정
    rdir = dir
    
    # left
    for i in range(num-1,-1,-1):            
        if left_check(q,i,i+1):    
            break
        else:                           # 다른 경우
            tmp[i].rotate(table[ldir])
            ldir = table[ldir]
            
    # right
    for i in range(num+1,n):            
        if right_check(q,i,i-1):      
            break
        else:
            tmp[i].rotate(table[rdir])
            rdir = table[rdir]
    q = tmp
    
#print(q)
res = 0
for i in range(len(q)):
    if q[i][0] == 1:
        res += 2**i
        
print(res)

    



    
    
    
    
    
            
            

    
    
    
    
    
