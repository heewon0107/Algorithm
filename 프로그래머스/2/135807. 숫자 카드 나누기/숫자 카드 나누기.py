def solution(arrayA, arrayB):
    def lcm(a, b):
        return a * b // gcd(a, b)            
    
    def gcd(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a
    
    def ngcd(array):
        result = array[0]
        if len(array) == 1:
            return result
        
        for i in range(1, len(array)):
            result = gcd(result, array[i])
        return result
    
    def can(n, array):
        if n == 1:
            return False
        
        for a in array:
            if a % n == 0:
                return False
        return True
        
    a_gcd = ngcd(arrayA)
    b_gcd = ngcd(arrayB)
    
    a = a_gcd if can(a_gcd, arrayB) else 0
    b = b_gcd if can(b_gcd, arrayA) else 0
    return max(a, b)