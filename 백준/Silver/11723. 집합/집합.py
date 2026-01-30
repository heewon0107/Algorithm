import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    command = input().strip()
    if command == 'all':
        s = set(range(1, 21))
        continue
    elif command == 'empty':
        s.clear()
        continue

    command, x = command.split()
    x = int(x)
    if command == 'add':
        s.add(x)
    elif command == 'remove':
        s.discard(x)
    elif command == 'check':
        print(1 if x in s else 0)
    elif command == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)