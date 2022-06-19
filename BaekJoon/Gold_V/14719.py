import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())        
arr = list(map(int,input().rstrip().split()))


answer = 0

# 첫번째와 마지막은 빗물이 고일 수 없으므로 제외
for i in range(1,m-1):
    
    left_max = max(arr[:i])     # i번째를 기준으로 왼쪽에서 가장 큰 값
    right_max = max(arr[i+1:])  # i번째를 기준으로 오른쪽에서 가장 큰 값
    
    if arr[i] < min(left_max,right_max):        # 왼쪽max와 오른쪽max의 최솟값과 비교
        answer += min(left_max,right_max) - arr[i]  # 더 작은 값에서 해당 i번의 높이만큼 빼준 값을 answer에 더한다.
        
print(answer)

        
    
