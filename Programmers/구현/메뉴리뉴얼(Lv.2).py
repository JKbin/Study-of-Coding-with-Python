orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
coures = [2,3,4]	

from itertools import combinations
from collections import Counter

def solution(orders,coures):
    answer = []
    
    for i in coures:
        temp = []
        for j in orders:
            j = sorted(j)
            temp.extend(list(combinations(j,i)))
            
        count = Counter(temp)
    
        if count:
            if max(count.values()) >= 2:
                for key,value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))
    return sorted(answer)


print(solution(orders,coures))