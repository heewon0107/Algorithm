def solution(k, tangerine):
    # 카운팅 정렬 후 sort
    N = max(tangerine) + 1
    arr = [0] * N
    
    # O(100000)
    for i in tangerine:
        arr[i] += 1
        
    arr.sort(reverse=True)
    answer = 0
    pick = 0
    idx = 0
    while pick < k and idx < N:
        pick += arr[idx]
        idx += 1
        answer += 1
    return answer