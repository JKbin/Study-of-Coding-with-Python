import re
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#files =  ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

def solution(files):
    
    for file in files:
        temp = [re.split(r'([0-9]+)',file) for file in files]
        
        sort = sorted(temp,key=lambda x:(x[0].lower(),int(x[1])))
        
        return [''.join(s) for s in sort]
        
        
print(solution(files))

    
