N = int(input())
cnt = 0
# N까지 순회하며 한수인지 체크
for i in range(1, N+1):
    # 한자리 숫자면 pass
    if i < 100:
        cnt += 1
        continue
    
    # 문자열로 바꿔주고 등차 수열인지 체크
    string = str(i)
    if int(string[0]) - int(string[1]) == int(string[1]) - int(string[2]):
        cnt += 1


print(cnt)