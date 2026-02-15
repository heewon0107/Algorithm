def solution(price):
    # 10만원은 5%, 30 => 10%, 50 => 20%
    discount = 0
    if price >= 5e5:
        discount = 0.2
    elif price >= 3e5:
        discount = 0.1
    elif price >= 1e5:
        discount = 0.05
    return int(price - price * discount)