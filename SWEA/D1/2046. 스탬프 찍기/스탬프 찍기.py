num = int(input())
if num < 0 or num >= 100000 :
    raise ValueError("주어질 숫자는 100,000 이하다.")

stamp = '#' * num
print(stamp)