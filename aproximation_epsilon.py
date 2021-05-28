objective = int(input('Choose an int: '))
epsilon = 0.01
paso = epsilon**2
ans = 0.0

# basicamente nos estamos acercando de a muy poco al objetivo
while abs(ans ** 2 - objective) >= epsilon and ans <= objective:
    # print(f'{ans} ** 2 = {ans**2} - {objective} = {ans**2 - objective}')
    ans += paso

if abs(ans ** 2 - objective) >= epsilon:
    print('No answer found')
else:
    print(f'sqrt of {objective} is {ans}')
