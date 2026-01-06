from itertools import permutations

def solution(numbers):
    def decimal(n):
        if n <= 1:
            return False
        for i in range(2, n//2 + 1):
            if not n % i:
                return False
        return True
    answer = set()
    for n in numbers:
        if decimal(int(n)):
            answer.add(int(n))
    
    # O(7 * 5040)
    for i in range(2, len(numbers)+1):
        for piece in list(permutations(list(numbers), i)):
            n = int(''.join(piece))
            if n not in answer and decimal(n):
                answer.add(n)
                
    return len(answer)