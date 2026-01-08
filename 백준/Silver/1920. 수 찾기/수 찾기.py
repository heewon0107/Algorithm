N = int(input())
A = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

A.sort()
answer = []
for n in lst:
    left = 0
    right = N-1
    can_find = False
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == n:
            can_find = True
            break
        elif A[mid] < n:
            left = mid + 1
        elif A[mid] > n:
            right = mid - 1

    answer.append('1' if can_find else '0')

print('\n'.join(answer))
