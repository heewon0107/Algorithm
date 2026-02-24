def solution(name, yearning, photo):
    answer = []
    score_lst = {}
    for n, x in zip(name, yearning):
        score_lst[n] = x
    
    for p in photo:
        score = 0
        for man in p:
            if man in score_lst:
                score += score_lst[man]
        answer.append(score)
    return answer