import sys

input = sys.stdin.readline

s = input().rstrip()

answer = []
st2 = []

for i in s:
    if i == '>':
        st2.append(i)
        answer.append(''.join(st2))
        st2.clear()
    elif i == '<':
        if st2:
            answer.append(''.join(st2[::-1]))
            st2.clear()
            st2.append(i)
        else:
            st2.append(i)
    else:
        if i == ' ' and '<' not in st2:
            answer.append(''.join(st2[::-1]))
            answer.append(' ')
            st2.clear()
        else:
            st2.append(i)
            
            
if st2:
    answer.append(''.join(st2[::-1]))


print(''.join(answer))



        
        
    


