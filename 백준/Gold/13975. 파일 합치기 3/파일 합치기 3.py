import heapq
def solution():
    T = int(input())

    for _ in range(T):
        N = int(input())
        lst = list(map(int, input().split()))
        heapq.heapify(lst)

        result = 0

        while len(lst) > 1:
            a = heapq.heappop(lst)
            b = heapq.heappop(lst)
            sum_ = a+b
            result += sum_
            heapq.heappush(lst, sum_)
        
        print(result)
        
    return 
solution()