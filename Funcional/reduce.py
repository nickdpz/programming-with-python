from functools import reduce
SELLS = [1, 1, 1, 10]


def run():
    total = reduce(lambda a, b: a+b, SELLS)
    print(total)


if __name__ == '__main__':
    run()
