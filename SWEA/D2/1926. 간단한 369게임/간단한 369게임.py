for i in range(1, int(input()) + 1):
    x = str(i)
    for r in x:
        if r in "369":
            if x in "----":
                x += "-"
            else:
                x = "-"
    print(x, end=" ")
