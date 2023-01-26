#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
import time


# Complete the time_delta function below.
def time_delta(t1, t2):
    # Sun 10 May 2015 13:54:36 -0700
    t1Object = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2Object = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    result = time.mktime(t1Object.utctimetuple()) - \
        time.mktime(t2Object.utctimetuple())
    return "{}".format(int(result))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
