
    
def solution(n, arr1, arr2):
    def cheat(s):
        
        if len(s) < n:
            s = ((n - len(s)) * "0") + s
    
        return s
    
    answer = [[" "] * n for _ in range(n)]
    
    
    for i in range(n):
        bin1 = cheat(bin(arr1[i])[2:])
        bin2 = cheat(bin(arr2[i])[2:])
        
        for j in range(n):
            if bin1[j] == "1" or bin2[j] == "1":
                answer[i][j] = "#"
                
        answer[i] = "".join(answer[i])
    return answer