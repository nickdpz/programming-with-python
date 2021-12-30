from time import sleep


def evenNumber(max: int):
    a: int = 0
    while True:
        if max <= a:
            raise StopIteration
        else:
            yield a
            a += 2


if __name__ == "__main__":
    numbers = evenNumber(5)
    for element in numbers:
        print(element)
        sleep(1)
    
