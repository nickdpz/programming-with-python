from time import sleep


def fibonacciGen(max: int):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if max <= a:
            raise StopIteration


if __name__ == "__main__":
    fibonacci = fibonacciGen(5)
    for element in fibonacci:
        print(element)
        sleep(1)
