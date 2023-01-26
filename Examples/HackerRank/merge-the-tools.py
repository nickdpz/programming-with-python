from typing import List
from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    results: List[str] = []
    for i in range(int(len(string)/k)):
        strTmp = "".join(OrderedDict.fromkeys(string[i*k:(i+1)*k]))
        print(strTmp)
        results.append(strTmp)
    return results
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)