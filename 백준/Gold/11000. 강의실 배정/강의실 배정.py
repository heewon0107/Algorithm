import heapq as hq
import sys
input = sys.stdin.readline
N = int(input())
# 사용중인 강의실 lst
lst = []
# 첫 강의
lectures = []

for _ in range(N):
    s, e = map(int, input().split())
    lectures.append((s, e))
    
lectures.sort(key=lambda x: x[0])

for s, e in lectures:
    if not lst:
        hq.heappush(lst, e)
        continue
    # 끝난 강의실 있나 확인
    if lst[0] <= s:
        hq.heappop(lst)
    # 새 강의실 등록
    hq.heappush(lst, e)

print(len(lst))