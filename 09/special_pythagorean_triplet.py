#!/usr/bin/python

import sys
from math import sqrt

def	find_value(search_val):
	for c in [x**2 for x in xrange(search_val / 2)]:
		for a in [y**2 for y in xrange(search_val)]:
			if a > c:
				break
			for b in [z**2 for z in xrange(search_val)]:
				if a + b == c and sqrt(a) + sqrt(b) + sqrt(c) == search_val:
					return a,b,c
				elif a + b > c:
					break

if len(sys.argv) > 1:
	search_val = int(sys.argv[1])
else:
	search_val = 1000

answer = find_value(search_val)
if answer != None:
	print 'answer: ' + str(int(sqrt(answer[0]) * sqrt(answer[1]) * sqrt(answer[2])))
else:
	print 'no solution'
