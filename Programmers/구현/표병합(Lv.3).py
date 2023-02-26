def solution(commands):
    answer = []
    
    n = 50
    
    parent = [[0]*(n+1) for i in range(n+1)]
    
    graph = [[None]*(n+1) for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            parent[i][j] = [i,j]
            
    
    for com in commands:
        com = com.split(' ')
        
        if com[0] == 'UPDATE':
            # 1. "UPDATE r c value"
            if len(com) == 4:
                r,c = int(com[1]), int(com[2])
                value = com[3]
                # 부모 셀 찾기
                px,py = parent[r][c]
                # 부모의 자식들 찾기
                son_list = []
                for i in range(1, n+1):
                    for j in range(1,n+1):
                        if parent[i][j] == [px,py]:
                            son_list.append([i,j])
                # 자식들 다 업데이트 하기
                for son in son_list:
                    graph[son[0]][son[1]] = value
            
            # "UPDATE value1 value2"
            # 1 -> 2로 변경
            elif len(com) == 3:
                value1, value2 = com[1], com[2]
                for i in range(1,n+1):
                    for j in range(1,n+1):
                        if graph[i][j] == value1:
                            graph[i][j] = value2
                            
        elif com[0] == 'MERGE':
            # "MERGE r1 c1 r2 c2"
            # r2,c2 -> r1,c1으로 병합
            # 둘 다 값이 있으면 r1,c1으로 초기화
            
            r1, c1, r2, c2 = int(com[1]), int(com[2]), int(com[3]), int(com[4])
            
            px1,py1 = None, None        # r1, c1의 부모
            px2,py2 = None, None        # r2, c2의 부모
            
            # 같은 셀이면 무시
            if [r1,c1] == [r2,c2]:
                continue
            
            # px1, py1 찾기
            px1, py1 = parent[r1][c1]
            # px2, py2 찾기
            px2, py2 = parent[r2][c2]
            
            value1 = graph[px1][py1]            # r1,c1의 value
            value2 = graph[px2][py2]            # r2,c2의 value
            
            # r2,c2의 자식들 찾기
            son_list2 = []
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if parent[i][j] == [px2,py2]:
                        son_list2.append([i,j])
                        
            # r1,c1의 자식들 찾기
            son_list = []
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if parent[i][j] == [px1,py1]:
                        son_list.append([i,j])
            
            # value 변경
            # [r1,c1]의 자식들 value2로 변경
            if value1 is None and value2 is not None:
                for s in son_list:
                    graph[s[0]][s[1]] = value2
            # [r2,c2]의 자식들 value1로 변경
            elif (value1 is not None and value2 is None) or (value1 is not None and value2 is not None):
                for s in son_list2:
                    graph[s[0]][s[1]] = value1
            
            # 부모 변경
            # [r2, c2] -> [r1, c1]
            for s in son_list2:
                parent[s[0]][s[1]] = [px1, py1]
            
        elif com[0] == 'UNMERGE':
            # "UNMERGE r c"
            r,c = int(com[1]), int(com[2])
            
            # [r,c]의 부모 찾기
            px1,py1 = parent[r][c]
            
            # value 찾기
            value = graph[r][c]
            
            # px1,py1의 자식 찾기
            son_list = []
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if parent[i][j] == [px1,py1]:
                        son_list.append([i,j])
                        
            
            # [r,c] 빼고 unmerge - value
            for s in son_list:
                x, y = s
                if [x, y] == [r, c]:
                    continue
                graph[x][y] = None
                
            # unmerge - parent
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if [i,j] in son_list:
                        parent[i][j] = [i,j]
                        
                        
            
        elif com[0] == 'PRINT':
            # "PRINT r c"
            r, c = int(com[1]), int(com[2])
            
            px1, py1 = parent[r][c]
            
            if graph[px1][py1] == None:
                answer.append("EMPTY")
            else:
                answer.append(graph[px1][py1])
    
    return answer