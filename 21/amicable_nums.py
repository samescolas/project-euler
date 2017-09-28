#!/usr/bin/python

import sys
from math import sqrt

def get_factors(n):
	factors = []
	for i in xrange(1, int((n / 2) + 1)):
		if n % i == 0:
			factors.append(i)
	return factors

DEFAULT_BOUND = 10000

# Because it's good practice to check for errors
try:
	upper_bound = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BOUND
except:
	upper_bound = DEFAULT_BOUND

amicables = {}

for n in xrange(1, upper_bound):
	factors = get_factors(n)
	n_sum = sum(factors)
	if n != n_sum and n_sum not in amicables and sum(get_factors(n_sum)) == n:
		amicables[n] = n_sum;
		amicables[n_sum] = n;

print("Total sum of amicables below {}: {}".format(upper_bound, sum(amicables.keys())))
