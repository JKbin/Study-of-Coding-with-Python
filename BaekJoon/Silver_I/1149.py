import sys

n = int(sys.stdin.readline().rstrip())
cost = []
for i in range(n):
    cost.append(list(map(int,sys.stdin.readline().rstrip().split())))




for i in range(1,len(cost)):
    # 빨간집인 경우
    cost[i][0] += min(cost[i-1][1],cost[i-1][2])
    # 초록집인 경우
    cost[i][1] += min(cost[i-1][0],cost[i-1][2])
    # 파란집인 경우
    cost[i][2] += min(cost[i-1][0],cost[i-1][1])
    
print(min(cost[-1]))


    
    