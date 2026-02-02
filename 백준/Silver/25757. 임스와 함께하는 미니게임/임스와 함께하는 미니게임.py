import sys
input = sys.stdin.readline
def solution():
    N, game = input().split()
    games = {
        'Y': 1,
        'F': 2,
        'O': 3
    }
    N = int(N)
    join = set()
    for _ in range(N):
        join.add(input())
    print(len(join) // games[game])

solution()