def run():
    superList = [
        {
            "name": "value"
        }
    ]

    for key in superList:
        print("Value key", key["name"])

    multiplesFourSixNine = [item*2 for item in range(
        0, 100)if item % 4 == 0 and item % 6 == 0 and item % 9 == 0]

    print("List Comprehensions result (map with filter)", multiplesFourSixNine)

    squareMulTwo = {item: item**(1/2)
                    for item in range(0, 10) if item % 2 == 0}

    print("Map Comprehensions result", squareMulTwo)


if __name__ == '__main__':
    run()
