def solution(cacheSize, cities):
    answer = 0
    cache=[]
    for city in cities:
        city=city.lower()
        if city not in cache:
            cache.append(city)
            answer += 5
            if len(cache)>cacheSize:
                del cache[0]
            
        else:
            cache.append(city)
            cache.remove(city)
            answer += 1
            
    return answer