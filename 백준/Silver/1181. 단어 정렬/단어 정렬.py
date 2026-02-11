import sys
input = sys.stdin.readline

def solution():

    N = int(input())
    lst = set(input().strip() for _ in range(N))
    lst = sorted(lst, key = lambda x: (len(x), x))

    print('\n'.join(lst))
solution()