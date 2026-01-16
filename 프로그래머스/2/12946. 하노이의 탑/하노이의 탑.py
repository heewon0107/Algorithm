def solution(n):
    answer = []
    
    def move(n, start, end, mid):
        # Finished, Remain 1
        if n == 1:
            answer.append([start, end])
            return
        
        # n-1 -> Sub Pole
        move(n-1, start, mid, end)
        
        # Biggest pole to End
        answer.append([start, end])
        
        # Mid to End
        move(n-1, mid, end, start)
            
    move(n, 1, 3, 2)
    return answer