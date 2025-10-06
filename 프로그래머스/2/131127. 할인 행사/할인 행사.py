def solution(want, number, discount):
    answer = 0
    n = len(want)
    # 5번 count
    for i in range(len(discount)-9):
        lst = discount[i:i+10]
        can_regi = True
        for j in range(n):
            if lst.count(want[j]) != number[j]:
                can_regi = False
                break
                
        if can_regi:
            answer += 1
    
    
    return answer