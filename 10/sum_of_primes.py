#!/usr/bin/python

import sys
from math import sqrt,ceil

def is_prime(n):
	maxval = int(ceil(sqrt(float(n))) + 1) 
	for p in xrange(2, maxval):
		if n % p == 0:
			return False
	return True

# loop through odd numbers and add to sum if prime
sum = 2
if len(sys.argv) > 1:
	for num in xrange(3, int(sys.argv[1]), 2):
		if is_prime(num):
			sum += num

print 'sum: ' + str(sum)
