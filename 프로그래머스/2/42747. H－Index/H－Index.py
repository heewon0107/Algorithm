def solution(citations):
    
    citations.sort(reverse=True)
    for i in range(len(citations)):
        # 인용값이 인용 편보다 작아야해
        if citations[i] < i + 1:
            return i
    # 아니면 
    return len(citations)