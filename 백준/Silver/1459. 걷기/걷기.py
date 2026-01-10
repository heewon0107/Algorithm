x, y, w, s = map(int, input().split())
result = 0
long = max(x, y)
short = min(x, y)
# 대각선이 비효율적
if s >= 2*w:
    result = (x+y) * w
elif s >= w:
    result = short * s + (long - short) * w
else:
    result = long * s
    # 홀수면
    if (x+y) % 2:
        result += (w - s)


print(result)
