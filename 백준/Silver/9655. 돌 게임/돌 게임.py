N = int(input())
# 마지막 돌을 가져가려면 내가 상대방에게 4개를 남겨줘야함.
# 선공이 홀수면 이긴다.
if N % 2:
    print('SK')
else:
    print('CY')