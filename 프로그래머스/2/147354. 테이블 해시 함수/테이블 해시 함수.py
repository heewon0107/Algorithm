def solution(data, col, row_begin, row_end):
    answer = 0
    
    #1. col - 1번째 컬럼 값 기준으로 오름차순 후 기본키 기준 내림차순
    data.sort(key = lambda x: (x[col-1], -x[0]))
    
    #2. row_begin -> row_end 까지 i로 나눈 나머지
    for i in range(row_begin-1, row_end):
        # mod 후 리스트 합
        answer = answer ^ sum(map(lambda x: x % (i+1), data[i]))
        
    return answer