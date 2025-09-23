def solution(board, skill):
    # type 1 = deal, type 2 = heal, r1,c1,r2,c2  degree
    
    # before code
    # maximum 250,000,000,000 2500억? -> 2차원 차이 배열 사용하자
    # for command in skill: # O(250000)
        # for i in range(command[1], command[3] + 1): # O(1000)
        #     for j in range(command[2], command[4] + 1): # O(1000)
        #         # deal
        #         if command[0] == 1:
        #             board[i][j] -= command[5]
        #         # heal
        #         elif command[0] == 2:
        #             board[i][j] += command[5]

        
    # after code
    # two-dimension Difference Array
    effect = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for command in skill: # O(250000)
        degree = -command[5] if command[0] == 1 else command[5]
        
        r1, r2, c1, c2 = command[1], command[3], command[2], command[4] 
        effect[r1][c1] += degree
        effect[r1][c2+1] -= degree
        effect[r2+1][c1] -= degree
        effect[r2+1][c2+1] += degree
        
    
    for j in range(len(effect[0])):
        for i in range(1, len(effect)):
                effect[i][j] += effect[i-1][j]
                
    for i in range(len(effect)):
        for j in range(1, len(effect[0])):
                effect[i][j] += effect[i][j-1]

                
    answer = 0
    # O(1000 X 1000)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + effect[i][j] > 0:
                answer += 1
        
    return answer