def solution(picks, minerals):
    fatigue = 0
    n = len(minerals)
    
    # 1. 5개씩 그룹으로 나누기
    groups = []
    for i in range(0, n, 5):
        mine = minerals[i:i+5]
        dia = mine.count('diamond')
        iron = mine.count('iron')
        stone = mine.count('stone')
        cost = 25*dia + 5*iron + stone
        groups.append((cost, mine))
        
    max_groups = sum(picks)
    groups = groups[:max_groups]
    
    # 2. 피로도 순 정렬
    groups.sort(reverse=True, key=lambda x: x[0])

    # 3. 곡괭이 순서 정하기
    pick_order = []
    for i, cnt in enumerate(picks):
        pick_order += [i] * cnt
    
    # 4. 광물 캐기
    for i in range(min(len(groups),len(pick_order))):
        mine = groups[i][1]
        pick = pick_order[i]
        
        for m in mine:
            if m == 'diamond':
                fatigue += [1,5,25][pick]
            elif m == 'iron':
                fatigue += [1,1,5][pick]
            else:
                fatigue += 1
    return fatigue
