from bisect import bisect_left
from itertools import combinations

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	

def solution(info,query):
    answer = []
    dicta = {}
    
    for inf in info:
        inf = inf.split()
        inf_key = inf[:-1]
        inf_value = int(inf[-1])
        
        for i in range(5):
            for c in combinations(inf_key,i):
                temp = ''.join(c)
                if temp not in dicta:
                    dicta[temp] = [inf_value]
                else:
                    dicta[temp].append(inf_value)
        
    for i in dicta:
        dicta[i].sort()
    
    
    for q in query:
        q = q.split()
        q_key = q[:-1]
        q_value = int(q[-1])
        
        while 'and' in q_key:
            q_key.remove('and')
        while '-' in q_key:
            q_key.remove('-')\
                
        z = ''.join(q_key)
        if z in dicta:
            scores = dicta[z]
            
            index = bisect_left(scores,q_value)
            answer.append(len(scores)-index)
        else:
            answer.append(0)
    return answer

        
        
            
            
        
        
                    
        
                
        
        
        
        
print(solution(info,query))

        
        

