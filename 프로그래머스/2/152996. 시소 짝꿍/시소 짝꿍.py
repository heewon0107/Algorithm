from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
    visited = [False] * 1001
    for w in weights:
        if visited[w]:
            continue
        visited[w] = True
        
        # 1. 1:1 비율
        if counter[w] > 1:
            # nC2
            answer += counter[w] * (counter[w] - 1) // 2
        # 2. 1:2 비율
        if 2 * w in counter:
            answer += counter[w] * counter[2*w]
        # 3. 2:3 비율
        if w * 3 % 2 == 0 and 3 * w // 2 in counter:
            answer += counter[w] * counter[3 * w // 2]
        # 4. 3:4 비율
        if w * 4 % 3 == 0 and 4 * w // 3 in counter:
            answer += counter[w] * counter[4 * w // 3]

        
    return answer