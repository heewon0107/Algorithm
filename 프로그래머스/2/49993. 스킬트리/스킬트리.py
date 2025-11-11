def solution(skill, skill_trees):
    answer = 0
    
    # O(5200)
    for s in skill_trees:
        # 1. 스킬 앞에서부터 탐색해
        skill_i = 0
        ski = skill[0]
        prev_i = s.find(ski)
        skill_i += 1
        
        # 2. 한 스킬트리 탐색
        can_go = True
        while skill_i < len(skill):
            # 스킬하나 선택
            ski = skill[skill_i]
            # 스킬 순서 찾기
            cur = s.find(ski)
            # 순서가 있다면
            if cur >= 0:
                # 이전 스킬 안 배움 or 이전 꺼 안 배움
                if prev_i == -1 or cur < prev_i:
                    can_go = False
                    break
                
            prev_i = cur
            skill_i += 1
                
        if can_go:
            answer += 1
        
    return answer