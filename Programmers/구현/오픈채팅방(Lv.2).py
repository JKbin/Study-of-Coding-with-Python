record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	


def solution(record):
    answer = []
    dicta = {}
    
    for i in record:
        a = i.split(' ')

        # 채팅방에 들어온 것
        if len(a) >= 3:
            dicta[a[1]] = a[2]
        
    for i in record:
        a = i.split()
    
        if a[0] == 'Enter':
            answer.append(dicta[a[1]]+'님이 들어왔습니다.')
        elif a[0] == 'Leave':
            answer.append(dicta[a[1]]+'님이 나갔습니다.')
    return answer

print(solution(record))

