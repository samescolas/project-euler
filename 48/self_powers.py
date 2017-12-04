#!/usr/local/bin/python3

from functools import reduce

# Python's so cool that this one isn't really a challenge
print(str(reduce(lambda x,y: x+y, [pow(n, n) for n in range(1, 1001)]))[-10:])
