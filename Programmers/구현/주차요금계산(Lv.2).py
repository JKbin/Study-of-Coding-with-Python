from math import ceil
temp_in = dict()

fees = [180, 5000, 10, 600]	
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	
# 시간 -> 분으로 변환
def ConvertoTime(time):
    s = time.split(':')
    minutes = int(s[0])*60 + int(s[1])
    return minutes

def solution(fees,records):
    answer = []
    result = []
    for i in records:
        if 'IN' in i:
            a = i.split(' ')
            minutes = ConvertoTime(a[0])
            if a[1] in temp_in:
                temp_in[a[1]].append( [minutes,'IN'] )
            else:
                temp_in[a[1]] = [[minutes,'IN']]
        else:
            a = i.split(' ')
            minutes = ConvertoTime(a[0])
            temp_in[a[1]].append([minutes,'OUT'])
            
    key_list = temp_in.keys()
    
    # 마지막 out이 없는 경우 23:59 out 추가하기
    for i in key_list:
        value_list = temp_in[i]
        if len(value_list) % 2 == 1:        
            add_out_time = ConvertoTime('23:59')
            temp_in[i].append([add_out_time,'OUT'])
            
    # 요금 계산
    for i in key_list:
        total_price,car_number = CalculateofFees(i,fees)
        result.append((total_price,car_number))
        
    result.sort(key=lambda x:x[1])
    for i in result:
        answer.append(i[0])
    return answer
    
# 요금계산        
def CalculateofFees(car_number,fees):
    value_list = temp_in[car_number]
    in_time = 0
    out_time = 0
    total_time = 0
    
    for i in value_list:
        if i[1] == 'IN':
            in_time += i[0]
        else:
            out_time += i[0]
    
    total_time = out_time - in_time
    
    if total_time <= fees[0]:
        return fees[1],car_number
    else:
        return (ceil((total_time-fees[0])/fees[2])*fees[3]) + fees[1],car_number
    
    
print(solution(fees,records))
