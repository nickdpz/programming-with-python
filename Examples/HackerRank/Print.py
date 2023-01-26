if __name__ == '__main__':
    n = int(input())
    i = 1
    acc = ""
    while (i <= n):
        acc = "{}{}".format(acc, i)
        i = i+1
    print(acc)
