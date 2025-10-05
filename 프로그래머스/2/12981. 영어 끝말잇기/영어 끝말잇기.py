def solution(n, words):
    told = set()               # 지금까지 말한 단어 저장
    told.add(words[0])         # 첫 단어는 무조건 통과
    
    for i in range(1, len(words)):
        # 1. 이미 말한 단어이거나
        # 2. 이전 단어의 마지막 글자와 현재 단어의 첫 글자가 다를 경우
        if words[i] in told or words[i-1][-1] != words[i][0]:
            player = (i % n) + 1         # 사람 번호 (1부터 시작)
            round_num = (i // n) + 1     # 라운드 수 (1부터 시작)
            return [player, round_num]
        
        told.add(words[i])

    return [0, 0]  
