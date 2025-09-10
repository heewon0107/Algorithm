def solution(enroll, referral, seller, amount):
    n = len(enroll)
    parents = {}
    profit = {}
    for i in range(n):
        profit[enroll[i]] = 0
        parents[enroll[i]] = referral[i] if referral[i] != "-" else None
    
    for i in range(len(seller)):
        current_seller = seller[i]
        current_cost = amount[i] * 100
        while current_seller and current_cost > 0:
            divide = current_cost // 10 
            mine =  current_cost - divide
            profit[current_seller] += mine

            current_seller = parents[current_seller]
            current_cost = divide
                   
    return list(profit.values())