str1 = 'FRANCE'
str2 = 'french'


# 다중집합으로 만들기
def jibhob(str1,str2):
    
    temp1 = []
    temp2 = ''
    temp3 = []
    temp4 = ''
    
    for i in range(len(str1)-1):
        temp2 = str1[i] + str1[i+1]
        
        if temp2.isalpha():
            temp1.append(temp2.lower())
            temp2 = ''
    
    for i in range(len(str2)-1):
        temp4 = str2[i] + str2[i+1]
        if temp4.isalpha():
            temp3.append(temp4.lower())
            temp4 = ''
    
    return temp1,temp3

# 합집합 및 교집합 구하기
def go_jibhob(arr1,arr2):
    
    hobjibhob = []
    kyojibhob = []
    
    for i in arr1:
        if i in arr2:
            kyojibhob.append(i)
            hobjibhob.append(i)
            arr2.remove(i)
        else:
            hobjibhob.append(i)
    
    for j in arr2:
        hobjibhob.append(j)
    
        
    return hobjibhob,kyojibhob

# 자카드 유사도 구하기
def jacard(hobjibhob,kyojibhob):
    
    try:
        return int((len(kyojibhob)/len(hobjibhob))*65536)
    except:
        return 65536

def solution(str1,str2):
    
    c,d = jibhob(str1,str2)
    e,f = go_jibhob(c,d)
    
    return jacard(e,f)

print(solution(str1,str2))