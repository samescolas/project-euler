#!/usr/local/bin/python3

import sys
from math import sqrt
from gmpy import is_square # C library for quick math things

if len(sys.argv) > 1:
	search_val = int(sys.argv[1])
else:
	search_val = 1000

def side_lengths(c, P):
	a = b = 1
	c2 = c**2
	# Search through integral values for a
	for search_a in range(1, c):
		test_b2 = c2 - (search_a**2)
		# If test_b2 is a perfect square, b is integral
		if is_square(test_b2):
			a,b = search_a, int(sqrt(test_b2))
			if sum([a, b, c]) == P:
				return a,b
	return False, False

max_abc = 0
max_P = 0
abc = []

# For each possibly Perimeter value P
# count the number of right triangles
# with integral sides
for P in range(1, search_val):
	search_bound = int(P/2)
	# For each possible value of c, the
	# hypotenuse, check for an integral
	# set of sides a,b such that sum(a, b, c)=P
	for c in range(search_bound):
		a,b = side_lengths(c, P)
		if a:
			abc.append((a, b, c))
	# Store P and max solutions if new maximum
	if len(abc) > max_abc:
		max_abc = len(abc)
		max_P = P
	abc = []

print ("There are {} solutions for P = {}.".format(max_abc, max_P))
