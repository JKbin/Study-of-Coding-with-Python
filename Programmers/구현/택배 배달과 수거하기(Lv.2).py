def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries = list(enumerate(deliveries,start=1))
    pickups = list(enumerate(pickups,start=1))

    while True:
        d = []
        d_cnt = 0
        while deliveries:
            if deliveries[-1][0] != 0 and d_cnt < cap:
                d_item = deliveries.pop()
                if d_cnt + d_item[1] > cap:
                    d.append((d_item[0], cap-d_cnt ))
                    deliveries.append( (d_item[0], d_cnt+d_item[1]-cap) )
                    d_cnt += cap-d_cnt
                else:
                    d_cnt += d_item[1]
                    d.append(d_item)
            else:
                break
        
        p = []
        p_cnt = 0
        while pickups:
            if pickups[-1][0] != 0 and p_cnt < cap:
                p_item = pickups.pop()
                if p_cnt + p_item[1] > cap:
                    p.append((p_item[0], cap-p_cnt))
                    pickups.append((p_item[0], p_cnt+p_item[1]-cap))
                    p_cnt += cap - p_cnt
                else:
                    p_cnt += p_item[1]
                    p.append(p_item)
            else:
                break
        
        while d and d[0][1] == 0:
            d.pop(0)
        while p and p[0][1] == 0:
            p.pop(0)
        
        # d는 있고 p가 없는 경우
        if d and not p:     
            answer += (d[0][0]*2)
        # d는 없고 p는 있는 경우
        elif not d and p:   
            answer += (p[0][0]*2)
        # 둘다 있는 경우
        elif d and p:       
            if d[0][0] > p[0][0]:
                answer += (d[0][0]*2)
            else:
                answer += (p[0][0]*2)
        
        if not deliveries and not pickups:
            break
    return answer