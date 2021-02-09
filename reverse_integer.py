def reverse(x):
    if x > 0:
        res = int(str(x)[::-1])
    if x <= 0:
        res = -1 * int(str(x*-1)[::-1])

    if(res >= -pow(2, 31) and res <= pow(2, 31)-1):
        return res
    else:
        return 0


print(reverse(246))
