def solution(storey):
    first = second = storey
    x = y = 0
    while first:
        num = first % 10
        first //= 10
        if num <= 5:
            x += num
        else:
            x += (10 - num)
            first += 1            
    
    while second:
        num = second % 10
        second //= 10
        if num < 5:
            y += num
        else:
            y += (10 - num)
            second += 1    
            
    return min(x, y)