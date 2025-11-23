while True:
    p = input()
    if p == '.':
        break
    m = len(p)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j and p[i] != p[j]:
            j = lps[j-1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j
    if m % (m-lps[-1]):
        print(1)
    else:
        print(m // (m - lps[-1]))