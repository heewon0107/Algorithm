def solution():

    def turn_on_off(i):
        switch[i] = 0 if switch[i] else 1

    # Number of Switch
    N = int(input())
    switch = list(map(int, input().split()))
    n_students = int(input())
    

    # O(100*100)
    for _ in range(n_students):
        sex, number = map(int, input().split())
        i = number - 1
        # Man
        if sex == 1:
            while i < N:
                turn_on_off(i)
                i += number
        # Woman
        elif sex == 2:
            turn_on_off(i)
            l = i - 1
            r = i + 1
            while 0 <= l and r < N and switch[l] == switch[r]:
                turn_on_off(l)
                turn_on_off(r)
                l -= 1
                r += 1
    for i in range(N):
        print(switch[i], end= ' ')
        if i % 20 == 19:
            print()

solution()