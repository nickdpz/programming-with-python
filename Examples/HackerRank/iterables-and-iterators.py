from typing import List
from functools import reduce

if __name__ == '__main__':
    k: int = int(input())
    string = "".join(input().split(" "))
    letterIndex = int(input())
    letterFound = 'a'
    combine: List[str] = ['{}{}'.format(string[i], string[j])
                          for i in range(k) for j in range(i+1, k)]
    results = reduce(lambda acu, item: acu +
                     1 if letterFound in item else acu, combine, 0)
    print(results/len(combine))
