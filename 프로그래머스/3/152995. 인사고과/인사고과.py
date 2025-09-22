def solution(scores):
    wanho = scores[0]
    wanho_total = sum(wanho)

    # Step 1: 완호가 받을 수 없는 경우 확인
    for score in scores:
        if score[0] > wanho[0] and score[1] > wanho[1]:
            return -1

    # Step 2: 유효한 지원자만 남기고, 총점 기준으로 순위 계산
    scores.sort(key=lambda x: (-x[0], x[1]))  # x점수는 내림차순, y는 오름차순
    max_y = 0
    answer = 1

    for score in scores:
        if score[1] < max_y:
            continue  # 지배당한 지원자 -> 인센티브 없음
        max_y = max(max_y, score[1])
        
        if sum(score) > wanho_total:
            answer += 1

    return answer
