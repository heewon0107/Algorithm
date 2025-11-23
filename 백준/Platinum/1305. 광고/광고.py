N = int(input())
advertisement = input()
m = len(advertisement)
lps = [0] * m
j = 0
for i in range(1, m):
    while j and advertisement[i] != advertisement[j]:
        j = lps[j-1]
    if advertisement[i] == advertisement[j]:
        j += 1
        lps[i] = j

print(N-lps[-1])