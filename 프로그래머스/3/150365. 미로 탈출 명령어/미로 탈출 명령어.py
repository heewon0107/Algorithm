def solution(n, m, x, y, r, c, k):
    # Impossible Pre-Processing
    distance = abs(r-x) + abs(c-y)
    if distance % 2 != k % 2 or distance > k:
        return 'impossible'
    
    # Index tuning
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    delta = [(1,0,'d'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    answer = []
    
    for i in range(1, k+1):
        for dx, dy, d in delta:
            nx, ny = x + dx, y + dy
            # Valid Check
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            remain = k - i
            dist = abs(r-nx) + abs(c-ny)
            if dist <= remain:
                answer.append(d)
                x, y = nx, ny
                break
        
    return ''.join(answer)