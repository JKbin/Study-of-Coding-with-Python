import sys

n = int(sys.stdin.readline().rstrip())
temp = []

for i in range(n):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    temp.append((x,y))
    
temp.sort(key=lambda x:(x[1],x[0]))



# s = start_time
# e = end_time
end = cnt = 0
    
for s,e in temp:
    if s >= end:
        cnt += 1
        end = e

print(cnt)


        
    
    




        


    
    


