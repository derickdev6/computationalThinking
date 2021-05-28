obj = int(input('Choose an in: '))
eps = 0.0000000001
lo = 0.0
hi = max(1.0, obj)

ans = (hi + lo) / 2

while abs(ans ** 2 - obj) >= eps:
    print(f'{ans} ** 2 = {ans**2}     -     lo {lo} - hi {hi}')
    if ans ** 2 < obj:
        lo = ans
    else:
        hi = ans

    ans = (hi + lo) / 2
print(ans)
