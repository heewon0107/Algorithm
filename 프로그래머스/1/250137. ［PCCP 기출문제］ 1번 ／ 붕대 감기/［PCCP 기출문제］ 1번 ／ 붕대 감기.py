from collections import deque
def solution(bandage, health, attacks):
    last_time = 0
    cur_health = health
    # 공격 패턴마다 남은 체력을 체크해야함
    for attack in attacks:
        # 지난 시간동안 힐량 체크
        heal_time = attack[0] - last_time - 1
        last_time = attack[0]
        
        cur_health += heal_time * bandage[1] + (heal_time // bandage[0]) * bandage[2]
        if cur_health > health:
            cur_health = health
        cur_health -= attack[1]

        # 체력이 없다면 break
        if cur_health <= 0:
            return -1
        
        
    return cur_health