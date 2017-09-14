#!/usr/bin/python

import sys
from math import sqrt
from functools import reduce

def triangle_number(n):
	ret = 0
	for i in range(1,n + 1):
		ret += i
	return ret

def get_factors(n):
	return set(reduce(list.__add__,
		([i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

if len(sys.argv) > 1:
	search_factors = int(sys.argv[1])
else:
	search_factors = 500
n = search_factors
search_val = triangle_number(n)
factors = get_factors(search_val)
print('searching for triangle number with ', n, 'factors')
while (len(factors) < search_factors):
	print(n, ':', search_val, ':', len(factors))
	search_val += n + 1
	factors = get_factors(search_val) 
	n += 1
print(n, search_val)
print('triangle number ', str(n) + ':', search_val, 'has ', len(factors), 'factors.')
