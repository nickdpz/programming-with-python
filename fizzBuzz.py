def fizzBuzz(n):
    # Write your code here
    i = 1
    while (n >= i):
        temp = ""
        if (i % 3 == 0):
            temp = "{}{}".format(temp, 'Fizz')

        if (i % 5 == 0):
            temp = "{}{}".format(temp, 'Buzz')

        if (temp == ""):
            print(i)
        else:
            print(temp)

        i = i+1


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
