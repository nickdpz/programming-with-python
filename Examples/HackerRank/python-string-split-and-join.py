from typing import List


def split_and_join(line):
    arrStr: List[str] = line.split(' ')
    return '-'.join(arrStr)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
