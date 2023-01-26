from typing import List, Dict
from functools import reduce


def getDistinct(accumulator: List[Dict], item: str):
    indexFound: int = -1
    accumulatorTmp = list(accumulator)

    for idx, dic in enumerate(accumulator):
        if dic['word'] == item:
            indexFound = idx
            break

    if (indexFound != -1):
        accumulatorTmp[indexFound] = {
            'count': accumulatorTmp[indexFound]['count']+1, 'word': accumulatorTmp[indexFound]['word']}
    else:
        accumulatorTmp.append({'count': 1, 'word': item})
    return accumulatorTmp


if __name__ == '__main__':
    t = int(input())
    listWords: List[str] = []

    for t_itr in range(t):
        word = input()
        listWords.append(word)

    results = reduce(getDistinct, listWords, [])
    resultsTmp = ['{}'.format(x['count']) for x in results]
    strTemp: str = ' '
    print(len(resultsTmp))
    print(strTemp.join(resultsTmp))
