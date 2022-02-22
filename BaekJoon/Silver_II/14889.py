from itertools import combinations
from sys import stdin


n = int(stdin.readline().rstrip())
graph = []
for i in range(n):
    graph.append(list(map(int,stdin.readline().rstrip().split())))


a = [i for i in range(n)]
b = list(combinations(a,n//2))


min_gap = 10000

for i in range(len(b)//2):
    team = b[i]
    stat_A = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_A += graph[member][k]
            
    team = b[-i-1]
    stat_B = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_B += graph[member][k]
            
    
    min_gap = min(min_gap,abs(stat_A-stat_B))
    
print(min_gap)








    
    
    
    






    
    


    



        

