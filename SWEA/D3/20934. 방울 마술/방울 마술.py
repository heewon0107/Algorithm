T = int(input())
for tc in range(1, T + 1):
    S, K = input().split()
    K = int(K)
    lst = [0] * 3
    for i in range(3):
        lst[i] = S[i]
    S = lst
    for i in range(K):
        if S[0] == "o":
            S[0], S[1] = S[1], S[0]
        elif S[1] == "o":
            S[0], S[1] = S[1], S[0]
        else:
            S[1], S[2] = S[2], S[1]
    for j in range(len(S)):
        if S[j] == "o":
            print(f"#{tc} {j}")
            break