#!/usr/bin/python

import sys
from math import pow

def factorial(n):
	if n < 1:
		return 1 
	return n * factorial(n - 1)

size = 20 if len(sys.argv) == 1 else int(sys.argv[1])

print("Number of paths on {}x{} grid: {}".format(size, size,
	int(factorial(2*size) / pow(factorial(size), 2))))
