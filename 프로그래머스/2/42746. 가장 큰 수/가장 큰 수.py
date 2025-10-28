def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key = lambda x: x*3)
    
    ans = ''
    for n in numbers:
        ans += n
    return str(int(ans))