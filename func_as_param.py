def main():
    numarr = [1, 2, 3]
    # I give the function another function as arg
    print(apply_operation(twox, numarr))
    print(apply_operation(twoplus, numarr))


def apply_operation(f, numarr):
    res = []
    for n in numarr:
        # Apply the function given as arg to every item in the array
        r = f(n)
        res.append(r)
    return res


def twox(n):
    return n * 2


def twoplus(n):
    return n + 2


if __name__ == '__main__':
    main()
