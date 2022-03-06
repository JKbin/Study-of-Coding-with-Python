import sys

input = sys.stdin.readline


n = int(input().rstrip())
#n = 2
#stra = ['GCF','ACDEB']
stra = []
for i in range(n):
    stra.append(input().rstrip())
temp = []
dicta = {}
for i in stra:
    for j in i:
        if j not in temp:
            temp.append(j)
            

for i in stra:
    for j in i:
        if j not in dicta:
            dicta[j] = 0
            

for i in stra:
    index = 0
    a = len(i)
    while a:
        dicta[i[index]] += 10**(a-1)
        index += 1
        a -= 1
        
c = sorted(dicta.items(), key=lambda x:x[1],reverse=True)       # value값으로 정렬

index = 0
res = 0
for i in range(9,9-len(temp),-1):
    res += c[index][1]*i
    index += 1
    
print(res)






    