def solution(n, computers):
    network = 0
    connected = [0] * n
    
    def is_network(computer):
        # 컴퓨터의 네트워크 연결
        connected[computer] = 1
        for i in range(n):
            if computers[computer][i] == 1 and not connected[i]:
                is_network(i)
            
    # i = 컴퓨터 번호
    for i in range(n):
        # i번째 컴퓨터를 들리지 않았다..
        if not connected[i]:
            # i번째 컴퓨터의 네트워크 연결
            is_network(i)
            network += 1
    
    return network
                
            

    
    