def solution(operations):
    q = []
    
    for command in operations:
        command1, command2 = command.split(" ")
        if command1 == "I":
            q.append(int(command2))
        else:
            if not q:
                continue
        
            q.sort()
            if command2 == "1":
                q.pop()
            elif command2 == "-1":
                q.pop(0)
                       
    if not q:
        return [0, 0]
    return [max(q), min(q)]