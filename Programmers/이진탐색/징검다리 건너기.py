stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3

def solution(stones, k):
    start = 1
    end = max(stones)               # 최대 건널 수 있는 사람의 수
    answer = 0
    
    
    while start <= end:
        mid = (start+end) // 2
        zero_count = 0              # 건널 수 없는 돌의 개수
        
        for st in stones:
            if st - mid <= 0:       # 사람 수 - 돌에 적혀있는 숫자 <= 0 : 그 돌은 건널 수 없음 
                zero_count += 1     # zero_count + 1 증가
            else:
                zero_count = 0      
            
            if zero_count >= k:     # 건널 수 없는 돌의 개수가 k개 이상이면 break
                break
        
        if zero_count < k:          # 아직 건널 수 있는 사람의 수가 더 있으므로 start 증가
            start = mid + 1
        else:                       # 건널 수 있는 사람의 수가 없으므로 end 감소
            end = mid - 1           
            answer = mid
    return answer


print(solution(stones,k))


                
    