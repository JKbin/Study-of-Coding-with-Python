from itertools import combinations, permutations, product
from collections import defaultdict

#users = [[40, 10000], [25, 10000]]	
#emoticons = [7000, 9000]	

#users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
#emoticons = [1300, 1500, 1600, 4900]


def solution(users, emoticons):
    answer = []
    
    discounts = [10, 20, 30, 40]
    
    for percents in product(discounts, repeat=len(emoticons)):
        #print(percents)
        tb = defaultdict(int)
        
        for i in range(len(users)):
            user_discount = users[i][0]
            user_total_amount = users[i][1]
            
            for j in range(len(percents)):
                percent = percents[j]
                if percent >= user_discount:     # 이모티콘 산다.
                    emoticon_price = emoticons[j] * ((100-percent)/100)
                    tb[i] += emoticon_price
                                                                                                            
        if tb:
            join_cnt = 0         # 가입자 수
            for k in tb:
                u = tb[k]   # 이모티콘 총 합
                user_total_amount = users[k][1]     # 이모티콘 마지 노선 금액
                
                if u >= user_total_amount:
                    join_cnt += 1
                    tb[k] = 0
            # 가입자 수, 사용자 총 이모티콘 금액
            #answer.append([join_cnt,sum(tb.values()), percents])
            answer.append([join_cnt,int(sum(tb.values()))])
            
            
    answer.sort(key=lambda x:(-x[0],-x[1]))
    return answer[0]
    
    # for i in answer:
    #     print(i)
        
    

                    
                    
            
            
            
                    
                     
                
                
                
    
