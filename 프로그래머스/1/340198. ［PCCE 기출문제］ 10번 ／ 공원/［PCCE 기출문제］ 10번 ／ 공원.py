def fn(i, j , n, park):
    # 시작 지점
    for ni in range(i, i + n):
        for nj in range(j, j + n):
            if park[ni][nj] != "-1":
                return False
    return True

def solution(mats, park):
    

    
    mats.sort(reverse=True)
    N = len(park)
    M = len(park[0])
    for n in mats: # O(10)
        # * O(2500)
        for i in range(N):
            # 매트보다 갈 공간이 작다.
            if N - i < n:
                break
            
            for j in range(M):
                if M - j < n:
                    break
                
                if park[i][j] == "-1":
                    # O(400)
                    if fn(i,j,n,park):
                        return n
        

    return -1