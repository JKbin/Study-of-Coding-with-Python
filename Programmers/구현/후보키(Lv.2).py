from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	

def solution(relation):
    answer = []

    n = len(relation)           # 행
    m = len(relation[0])        # 열

    # 유일성 검사
    for i in range(m):
        temp = []
        for j in range(n):
            if relation[j][i] not in temp:
                temp.append(relation[j][i])
            else:
                break
        else:
            answer.append({i})

    # table 초기화
    table = dict()
    for i in range(m):
        table[i] = []
    for i in range(m):      # 4
        for j in range(n):  # 6
            table[i].append(relation[j][i]) 

    # 최소성 검사
    for i in range(2, m+1):
        for j in combinations(table.keys(), i):
            j = set(j)

            # answer에 있는 것들 먼저 검사
            for a in answer:
                if a.issubset(j):           # 하위집합인지 검사하는 함수! superset()은 상위집합이 될 수도 있는지 검사하는 함수 
                    break
            else:
                # 검사 시작
                j = list(j)
                tp = []
                for jk in j:
                    tp.append(table[jk])

                t = list(zip(*tp))
                tp = {}
                for ss in t:
                    if ss not in tp:
                        tp[ss] = 1
                    else:
                        break
                else:
                    answer.append(set(j))
    return len(answer)

solution(relation)
