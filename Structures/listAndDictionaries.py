def run():
    superList = [
        {
            "name": "value"
        }
    ]

    for key in superList:
        print(key["name"])

    multiplesFourSixNine = [item for item in range(
        0, 100)if item % 4 == 0 and item % 6 == 0 and item % 9 == 0]
    
    print(multiplesFourSixNine)

    squareMulTwo = {item: item**(1/2)
                 for item in range(0, 10) if item % 2 == 0}

    print(squareMulTwo)


if __name__ == '__main__':
    run()
