S = input()
items = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        items.add(S[i:j])

print(len(items))
