def main():
    a = 1

    def nested():
        print(a)
    return nested


def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier


if __name__ == "__main__":
    my_func = main()
    my_func()
    times10 = make_multiplier(10)
    times4 = make_multiplier(4)
    print(times10(3))  # => 10 * 3 = 30
    print(times4(5))  # => 4 * 5 = 20
    print(times10(times4(2)))  # => 4 * 2 * 10 = 80
