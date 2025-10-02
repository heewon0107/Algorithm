def solution(n, w, num):
    import math
    
    target = (0,0)
    # 층 수
    h = math.ceil(n / w)
    
    arr = [[0] * w for _ in range(h)]
    
    right = False
    number = 1
    for i in range(h):
        if number > n:
            break
        right = not right
        for j in range(w):
            if number > n:
                break
            
            col = j if right else w - j - 1
             
            arr[i][col] = number
                
            if number == num:
                target = (i,col)
                
            number += 1
            
    result = 0
    row, col = target[0], target[1]
    while row < h and arr[row][col] != 0:
        result += 1
        row += 1
        
    return result