files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
def solution(files):
    temp = []
    answer = []
    
    
    
    for word in files:
        head = ''
        number = ''
        tail = ''
        check = False
        # 1. 문자열을 head,number,tail로 구분하기
        for j in range(len(word)):
            if word[j].isdigit():
                number += word[j]
                check = True
            elif not check:
                head += word[j]
            else:
                tail = word[j:]
                break
        # 2. 튜플 형태로 배열에 저장        
        temp.append((head,number,tail))
    # 3. 문제에 주어진 조건대로 정렬
    temp.sort(key=lambda x:(x[0].upper(),int(x[1])))
    
    for i in temp:
        temp2 = ''
        for j in i:
            temp2 += str(j)
        answer.append(temp2)
    return answer


print(solution(files))

