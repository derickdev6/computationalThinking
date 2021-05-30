def main():
    print(operate(int(input('Type a number: '))))


def operate(n):
    operations = [abs, double, half, x10]
    res = []
    for op in operations:
        res.append(op(n))
    return res


def double(x):
    return 2*x


def half(x):
    return x/2


def x10(x):
    return x*10


if __name__ == '__main__':
    main()
