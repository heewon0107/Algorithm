text = input()
pattern = input()

m = len(pattern)
lps = [0] * m
j = 0

for i in range(1, m):
    while j and pattern[i] != pattern[j]:
        j = lps[j-1]
    if pattern[i] == pattern[j]:
        j += 1
        lps[i] = j

i = j = 0
cnt = 0
result = []
while i < len(text):
    if text[i] == pattern[j]:
        i += 1
        j += 1
        if j == m:
            cnt += 1
            result.append(i - m + 1)
            j = lps[j-1]
    else:
        if j:
            j = lps[j-1]
        else:
            i += 1
print(cnt)
for r in result:
    print(r, end = ' ')