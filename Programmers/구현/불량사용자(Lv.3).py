from itertools import permutations


# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
# banned_id = ["fr*d*", "abc1**"]	

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
banned_id = ["*rodo", "*rodo", "******"]	

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
# banned_id = ["fr*d*", "*rodo", "******", "******"]	


def check(u_id,b_id):
    
    for i in range(len(b_id)):
        if len(u_id[i]) != len(b_id[i]):
            return False
        for j in range(len(u_id[i])):
            if b_id[i][j] != '*':
                if u_id[i][j] != b_id[i][j]:
                    return False
    return True
    



def solution(user_id, banned_id):
    answer = []
    
    for i in permutations(user_id,len(banned_id)):
        if check(i,banned_id):
            if set(i) not in answer:
                answer.append(set(i))
            
    return len(answer)



print(solution(user_id,banned_id))

