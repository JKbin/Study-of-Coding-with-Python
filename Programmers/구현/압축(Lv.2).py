import string
msg = 'KAKAO'

def solution(msg):
    answer = []
    a = list(string.ascii_uppercase)
    dicta = {}

    for i in range(len(a)):
        dicta[a[i]] = i+1
        
    w,z = 0,0

    while True:
        z += 1
    
        if z == len(msg):
            answer.append(dicta[msg[w:z]])
            break
        else:
            if msg[w:z+1] not in dicta:
                dicta[msg[w:z+1]] = len(dicta) + 1
                answer.append(dicta[msg[w:z]])
                w = z
                
    return answer

print(solution(msg))

