def solution(wallet, bill):
    answer = 0
    while max(wallet) < max(bill) or min(wallet) < min(bill):
        if bill[0] < bill[1]:
            bill[1] //= 2
        else:
            bill[0] //= 2
        answer += 1
        
    return answer