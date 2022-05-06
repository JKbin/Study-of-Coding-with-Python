cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	


def solution(cacheSize, cities):
    answer = 0
    cache = []
    miss = 5
    hit = 1
    
    if cacheSize == 0:
        answer += len(cities)*miss
        return answer
    
    for city in cities:
        city = city.lower()
        if city not in cache:       # miss      
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += miss
            
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += hit
    return answer
                
                
print(solution(cacheSize,cities))     

            
        
        
    
    