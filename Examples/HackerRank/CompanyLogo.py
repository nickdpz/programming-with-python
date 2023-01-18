#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce 
from typing import Dict, List
import re


def getNumberLetters(a,b):
    result: List[Dict] = a['result']
    countString = len(re.findall(b,a['current']))
    current:str=a['current']
    if(countString):
        current=a['current'].replace(b,'')
        result.append({'letter':b,'count':countString})
    return {'current':current, 'result':result}
    
    
if __name__ == '__main__':
    s = input()
    results= reduce(getNumberLetters, s, {'current':s,'result':[]})
    letterArray: List[Dict] = results['result']
    letterArray.sort(key=lambda x: (-x['count'], x['letter']))
    for i in range(3):
        print('{} {}'.format(letterArray[i]['letter'],letterArray[i]['count']))
    