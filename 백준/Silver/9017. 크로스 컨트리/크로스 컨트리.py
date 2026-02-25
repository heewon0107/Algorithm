
def solution():
    # 1. 여섯 명의 선수로 구성되어야함.
    # 2. 동점의 경우 다섯 번째 주자 고려
    # 3. 가장 낮은 점수 팀 우승

    
    for tc in range(int(input())):
        N = int(input())
        ranking = list(map(int, input().split()))

        # 마지막 팀 넘버
        max_val_team = max(ranking)

        # 팀 당 스코어 모음
        score = [[] for _ in range(max_val_team + 1)]

        # 팀 스코어 판단 배열 if num >= 6
        can_score = [False] * (max_val_team + 1)
        for team in range(1, max_val_team + 1):
            if ranking.count(team) >= 6:
                can_score[team] = True

        # 점수 넣어주기 O(1000)
        point = 1
        for team in ranking:
            # 6명 이상인 팀이다.
            if can_score[team]:
                score[team].append(point)
                point += 1

        min_team = 1
        min_score = 1e9
        for team, lst in enumerate(score):
            # 제외한 팀 패스
            if not lst:
                continue
            
            cur_score = sum(lst[:4])
            # 팀과 최대점수 갱신
            if min_score > cur_score:
                min_score = cur_score
                min_team = team
            # 새로운 팀이 더 일찍 들어왔
            elif min_score == cur_score:
                if score[min_team][4] > score[team][4]:
                    min_team = team
        print(min_team)
solution()