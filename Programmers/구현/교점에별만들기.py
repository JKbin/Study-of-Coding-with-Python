

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	


def calc(i,j):
    A = i[0]
    B = i[1]
    E = i[2]
    C = j[0]
    D = j[1]
    F = j[2]
    
    if (A*D) - (B*C) != 0:
        x =  ((B*F)-(E*D)) / ((A*D)-(B*C))
        y =  ((E*C)-(A*F)) / ((A*D)-(B*C))
        
        if abs(x) % 2 == 0 or abs(x) % 2 == 1:
            if abs(y) % 2 == 0 or abs(y) % 2 == 1:
                return(int(x),int(y))
            
        




def solution(line):
    answer = []
    
    temp = []
    n = len(line)
    for i in range(n):
        for j in range(i,n):
            if i != j:
                k = calc(line[i],line[j])
                if k != None:
                    temp.append(k)
    x_min, x_max, y_min, y_max = min(temp)[0],max(temp)[0],min(temp,key = lambda x: x[1])[1],max(temp,key = lambda x: x[1])[1]
    
    graph = [['.']*(abs(x_max-x_min)+1) for _ in range((abs(y_max-y_min)+1))]
    
    for a,b in temp:
        x = abs(y_max-b)
        y = abs(x_min-a)
        graph[x][y] = '*'
        
    for i,v in enumerate(graph):
        graph[i] = ''.join(v)
    return graph


print(solution(line))

    