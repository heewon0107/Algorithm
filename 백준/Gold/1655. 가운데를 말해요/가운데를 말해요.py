import heapq as hq
import sys
input = sys.stdin.readline
left_q = []
right_q = []
# O(100,000)
for i in range(int(input())):
    # Input Num
    num = int(input())
    
    if i % 2:
        hq.heappush(right_q, num)
    else:
        hq.heappush(left_q, -num)
    
    if right_q and -left_q[0] > right_q[0]:
        hq.heappush(right_q, -hq.heappop(left_q))
        hq.heappush(left_q, -hq.heappop(right_q))


    print(-left_q[0])