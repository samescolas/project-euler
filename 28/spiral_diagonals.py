#!/usr/bin/python

from math import pow
import sys

DEFAULT = 1001

try:
	UBOUND = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT

except:
	UBOUND = DEFAULT

total = 1
len = 2
for i in range(3, UBOUND + 1, 2):
	layer = 2*pow(i, 2) - 4*(len-1)
	total += (2*layer - (4*(len-1)))
	len += 1

print(int(total))
