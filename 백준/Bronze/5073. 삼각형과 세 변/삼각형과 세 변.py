def solution():
    while True:
        a, b, c = map(int, input().split())
        # 0 => Finish
        if not a and not b and not b:
            return
        
        num = sorted([a, b, c])
        if num[-1] >= num[0] + num[1]:
            print('Invalid')
        elif a == b and b == c:
            print('Equilateral')
        elif a == b or b == c or a == c:
            print('Isosceles')
        else:
            print('Scalene')

solution()