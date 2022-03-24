s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"	

def solution(s):
    answer = []
    
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    
    for i in s:
        a = i.split(",")
        
        for k in a:
            if int(k) not in answer:
                answer.append(int(k))
    return answer
print(solution(s))

