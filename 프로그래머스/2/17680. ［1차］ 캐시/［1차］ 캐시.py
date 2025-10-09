def solution(cacheSize, cities):
    # 빈도 적은 값 지우기 LRU
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        # 캐시에 있다.
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        # 캐시에 없다.
        else:
            answer += 5
            cache.append(city)
            
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer