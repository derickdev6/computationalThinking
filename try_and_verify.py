objective = int(input('choose an int: '))
ans = 0

while (ans ** 2 < objective):
    # print(f'{ans} ** 2 = {ans**2}')
    ans += 1

if ans ** 2 == objective:
    print(f'The sqrt of {objective} is {ans}')
else:
    print(f'The objective {objective} has no sqrt')
