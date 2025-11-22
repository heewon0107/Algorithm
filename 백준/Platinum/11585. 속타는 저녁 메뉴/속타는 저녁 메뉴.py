def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r 

    return a

N = int(input())
p = input().split()
circle = input().split()

m = len(p)
lps = [0] * m
j = 0
for i in range(1, m):
    while j and p[i] != p[j]:
        j = lps[j-1]
    
    if p[i] == p[j]:
        j += 1
        lps[i] = j

circle += circle
i = j = 0
cnt = 0

while i < len(circle)-1:
    if circle[i] == p[j]:
        i += 1
        j += 1
        if j == m:
            cnt += 1
            j = lps[j-1]
    else:
        if j:
            j = lps[j-1]
        else:
            i += 1

# 최소 공배수 찾기
g = gcd(N, cnt)
if g:
    print(f'{cnt // g}/{N // g}')

else:
    print(f'1/{N // cnt}')