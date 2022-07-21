from copy import deepcopy
import sys

input = sys.stdin.readline

N,M,K = map(int,input().rstrip().split())
table = dict()
for _ in range(M):
    data = list(map(int,input().rstrip().split()))
    r1,c1,m1,s1,d1 = data[0]-1,data[1]-1,data[2],data[3],data[4]
    table[(r1,c1)] = [[m1,s1,d1]]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

# N,M,K = 4,2,1
# table = {(0, 0): [[5, 2, 2]], (0, 3): [[7, 1, 6]]}


# 이동
def move():
    global table
    tmp = dict()
    for key in table:
        prev_x,prev_y = key
        
        for v in table[key]:
            # 질량,속력,방향
            prev_m,prev_s,prev_d = v
            
            move_x = (prev_x + dx[prev_d]*prev_s) % N           # 각 열과 행은 연결되어 있음(주의)
            move_y = (prev_y + dy[prev_d]*prev_s) % N
            
            if (move_x,move_y) not in tmp:
                tmp[(move_x,move_y)] = [[prev_m,prev_s,prev_d]]
            else:
                tmp[(move_x,move_y)].append([prev_m,prev_s,prev_d])
    
    table = deepcopy(tmp)
    
    
    
def fun():
    global table
    tmp = dict()
    for key in table:
        if len(table[key]) >= 2:
            sum_m,sum_s = 0,0
            odd = False
            Even = False
            
            for v in table[key]:
                ma,sa,da = v
                sum_m += ma         # 총 질량
                sum_s += sa         # 총 속력
                
                # 방향 정의
                if da % 2 == 0:
                    Even = True
                else:
                    odd = True
            
            if odd == Even:
                after_d = [1,3,5,7]
            else:
                after_d = [0,2,4,6]

            # even : True, Odd : False => 모두 짝수 : [0,2,4,6]
            # even : False, Odd : True => 모두 홀수 : [0,2,4,6]
            # even : True, Odd : True => 다름 : [1,3,5,7]
            
            
            
            
            for i in after_d:
                if sum_m // 5 > 0:
                    if key not in tmp:
                        tmp[(key)] = [[sum_m//5,sum_s//len(table[key]),i]]
                    else:
                        tmp[(key)].append([sum_m//5,sum_s//len(table[key]),i])
            
        else:
            a1,b1 = key
            tmp[(a1,b1)] = table[key]
            
    table = deepcopy(tmp)
            
            
ans = 0                

while K:
    K -= 1
    
    move()
    fun()
    
for k in table:
    for v in table[k]:
        ans += v[0]
        

print(ans)


        
    
    







         
    

                
                
                
            
                
            
            
            
            
            
        
                
                
                
            
        
    
    
    
            
        
        
        
                
                
                

                
                
                    
                
                
                
                
                

                
        
         
        




    




        

        



        
    
