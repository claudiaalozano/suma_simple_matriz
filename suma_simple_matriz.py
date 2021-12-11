import math
import os
import random
import re
import sys

def simpleArraySum(ar):

if __name__ == "__main__":
    ftpr = open(os.environ["OUTPUT_PATH"], "W")

    ar_count = int(input().strip())
    ar=list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + "\n")

    fptr.close()