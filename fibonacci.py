def main():
    limit = int(input('Type a limit: '))
    print(fibonacciLimit(limit))
    print(fibonacciRepetitions(limit))


def fibonacciLimit(limit, a=0, b=1):
    c = a + b
    print(f'{a} + {b} = {c}')
    if(a+b >= limit):
        return c
    else:
        return fibonacciLimit(limit, b, c)


# Very unneficient
def fibonacciRepetitions(x):
    if x == 0 or x == 1:
        return 1
    else:
        print(f'{x-1} + {x-2} = {(x-1)+(x-2)}')
        return fibonacciRepetitions(x-1) + fibonacciRepetitions(x-2)


if __name__ == '__main__':
    main()
