def solution(brown, yellow):
    total = brown + yellow
    answer = [0, 0]
    width = total
    while width > 0:
        width -= 1
        if total % width:
            continue
        
        height = total / width
        y = (width - 2) * (height - 2)
        b = total - y
        if y == yellow and b == brown:
            answer[0] = width
            answer[1] = height
            break
    
        
    return answer