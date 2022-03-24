p = "(()())()"


def olbalen(s):
    
    stack = []
    
    for i in s:
        if i =='(':
            stack.append(i)
        elif i ==')' and len(stack) > 0:
            stack.pop()
            
    if len(stack) == 0:
        return True         # 균형잡힌 문자열이면 True
    return False            


def divide(s):
    
    num_i = 0       # '('
    num_j = 0       # ')'
    
    for i in range(len(s)):
        if s[i] == '(':
            num_i += 1
        else:
            num_j += 1
            
        if num_i == num_j:
            return s[:i+1],s[i+1:]
    return False




def solution(p):
    
    # 1단계
    if not p:
        return ""
    
    # 2단계
    u,v = divide(p)
    
    # 3단계
    if olbalen(u):
        return u + solution(v)
    # 4단계
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        
        for i in u[1:len(u)-1]:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        return temp
    
print(solution(p))
