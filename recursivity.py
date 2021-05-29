def main():
    x = int(input('Type a number: '))
    print(factorial(x))


def factorial(x):
    if x == 1:
        return x
    elif x < 1:
        return 0
    else:
        print(x)
        return x * factorial(x-1)


if __name__ == '__main__':
    main()
