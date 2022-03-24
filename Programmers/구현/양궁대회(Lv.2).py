from itertools import combinations_with_replacement
n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]		

def solution(n,info):
    answer = [0 for i in range(0,11)]
    win = False
    check = 0

    # 중복 조합을 이용한 점수 만들기
    for score in list(combinations_with_replacement(range(0,11),n)):
    
    # 라이언의 점수
        now = [0 for i in range(0,11)]
    
        for i in score:
            now[10-i] += 1
        
        lion = 0
        apeach = 0
    
    # 라이언과 어피치 점수 비교
        for i,(l,p) in enumerate(zip(now,info)):
            if l == p == 0:
                continue
            if p >= l :
                apeach += (10 - i)
            elif p < l :
                lion += (10 - i)
            
    # 총 점수 비교
        if lion > apeach:
            win = True
        
        
            if (lion - apeach) > check:
                check = (lion - apeach)
                answer = now
            
    if not win:
        return [-1]
    else:
        return answer
    
    
print(solution(n,info))
