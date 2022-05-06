gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	
#gems = ["AA", "AB", "AC", "AA", "AC"]	
#gems = ["XYZ", "XYZ", "XYZ"]	
#gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	

def solution(gems):
    answer = []
    
    m = len(set(gems))
    n = len(gems)+1
    
    dicta = dict()
    
    start = 0
    end = 0
    
    while end < len(gems):
        
        if gems[end] not in dicta:
            dicta[gems[end]] = 1
        else:
            dicta[gems[end]] += 1
        end += 1
        
        
        if len(dicta) == m:
            while start < end:
                if dicta[gems[start]] > 1:
                    dicta[gems[start]] -= 1
                    start += 1
                
                elif n > end - start:
                    n = end - start
                    answer = [start+1,end]
                    break
                else:
                    break
    return answer
            
                    

# DIA, RUBY, EMERALD,SAPPHIRE
print(solution(gems))

