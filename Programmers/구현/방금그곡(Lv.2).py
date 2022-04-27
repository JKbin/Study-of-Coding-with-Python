# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	

m = "CC#BCC#BCC#BCC#B"	
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	

# m = 'ABC'
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	

def code_chagne(code):
    temp = code.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return temp
            
def convertToTime(s):
    s = s.split(':')
    return int(s[0])*60 + int(s[1])    


def calc(time,a):
    n = len(a)
    mod = divmod(time,n)
    temp = a * (mod[0]) + a[:mod[1]]
    return temp


def solution(m,musicinfos):
    music_answer = []
    
    for i in range(len(musicinfos)):
        info = musicinfos[i].split(",")
        start_time = info[0]
        end_time = info[1]
        title = info[2]
        play_code = info[3]
        
        change_code = code_chagne(m)                # 기억한 멜로디
        play_change_code = code_chagne(play_code)       # 악보의 # 변환
        
        total_time = convertToTime(end_time)-convertToTime(start_time)
        total_code = calc(total_time,play_change_code)
        
        if change_code in total_code:
            music_answer.append([total_time,i,title])
            
            
    if not music_answer:
        return '(None)'
    else:
        music_answer.sort(key=lambda x:(-x[0],x[1]))
        return music_answer[0][2]
    
    
print(solution(m,musicinfos))
