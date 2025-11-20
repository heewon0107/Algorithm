import heapq
    
for tc in range(1, int(input())+1):
    N = int(input())
    heap = []
    
    result = '#'+ str(tc) + ' '

    for _ in range(N):
        lst = list(map(int, input().split()))

        if lst[0] == 1:
            heapq.heappush(heap, -lst[1])
        else:
            if heap:
                num = -heapq.heappop(heap)
            else:
                num = -1
            result += str(num) + ' '
    print(result)