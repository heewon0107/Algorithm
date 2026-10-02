def solution(numbers, hand):
    answer = ''
    left = (3,0)
    right = (3,2)
    
    location = [(3,1)]
    for i in range(3):
        for j in range(3):
            location.append((i, j))
                
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left = location[number]
        elif number in [3,6,9]:
            answer += 'R'
            right = location[number]
        else:
            r, c = location[number]
            l = abs(left[0] - r) + abs(left[1] - c)
            r = abs(right[0] - r) + abs(right[1] - c)
            if l < r:
                answer += 'L'
                left = location[number]
            elif r < l:
                answer += 'R'
                right = location[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = location[number]
                elif hand == 'right':
                    answer += 'R'
                    right = location[number]
    
    return answer