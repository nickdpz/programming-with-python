from typing import List

if __name__ == '__main__':
    inputList: List[any] = []
    scores: List[int] = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        inputList.append([name, score])
    scores = list(set(scores))
    scores.sort()
    outputList: List[str] = [x[0]
                             for x in inputList if (x[1] == scores[1])]
    outputList.sort()
    for x in outputList:
        print(x)
