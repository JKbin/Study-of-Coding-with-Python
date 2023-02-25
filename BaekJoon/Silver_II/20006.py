import sys

input = sys.stdin.readline

p, m = map(int, input().rstrip().split())

rooms = [[] for i in range(300+1)]
level_limit = {}

room_index = 0

for _ in range(p):
    level, id = input().rstrip().split()
    level = int(level)
    
    join = False                        # 내가 방에 들어갔는지 안 들어갔는지에 대한 flag
    if not level_limit:
        rooms[room_index].append([room_index,level,id])
        level_limit[room_index] = [level-10, level+10]
    else:
        # 나에게 맞는 level limit 찾기
        for rm_idx in level_limit:
            min_level = level_limit[rm_idx][0]
            max_level = level_limit[rm_idx][1]
            
            # 정원이 아직 미달인 경우만 넣기
            if len(rooms[rm_idx]) < m:
                if min_level <= level and level <= max_level:
                    rooms[rm_idx].append([rm_idx,level,id])
                    join = True
                    break
        
        if not join:
            room_index += 1
            level_limit[room_index] = [level-10, level+10]
            rooms[room_index].append([room_index,level,id])
            
    


for room in rooms:
    if room:
        room.sort(key=lambda x:x[2])
        if len(room) == m:
            print('Started!')
        elif len(room) < m:
            print('Waiting!')
        for r_idx, level, id in room:
            print(f'{level} {id}')
    else:
        break
            
            
            
            
                
    

            
        
        
            
            
            
    

        
        

        
    
    
    




