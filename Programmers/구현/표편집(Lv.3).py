n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	
# linkedlist 구현

def solution(n, k, cmd):
    answer = ['O']*n
    cur = k
    table = {i:[i-1,i+1] for i in range(n)}
    
    table[0] = [None,1]
    table[n-1] = [n-2,None]
    stack = []
    
    for c in cmd:
        if c == 'C':
            answer[cur] = 'X'
            pre,next = table[cur]
            stack.append((pre,cur,next))
            
            if pre == None:
                table[next][0] = None
            elif next == None:
                table[pre][1] = None
            else:
                table[pre][1] = next
                table[next][0] = pre
                
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            
        elif c == 'Z':
            pre,now,next = stack.pop()
            answer[now] = 'O'
            
            if pre == None:
                table[next][0] = now
            elif next == None:
                table[pre][1] = now
            else:
                table[pre][1] = now
                table[next][0] = now
            
            
            
        else:
            c = c.split()
            if c[0] == 'D':
                for i in range(int(c[1])):
                    cur = table[cur][1]
            else:
                for i in range(int(c[1])):
                    cur = table[cur][0]
                
    return "".join(answer)


print(solution(n,k,cmd))
