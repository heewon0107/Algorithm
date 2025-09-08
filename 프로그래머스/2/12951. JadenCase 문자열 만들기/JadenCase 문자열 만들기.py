def solution(s):
    lst = s.split(" ")
    answer = []
    
    for word in lst:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append("")
            
    return " ".join(answer)
