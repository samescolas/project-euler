#!/usr/bin/python

import sys

class FibNum:
	def __init__(self):
		self.lo = 1
		self.hi = 1

	def __iter__(self):
		return self

	def next(self):
		fib = self.lo
		self.lo, self.hi = self.hi, self.lo + self.hi
		return fib
		

DEFAULT_DIGITS = 1000

try:
	DIGITS = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIGITS
except:
	DIGITS = DEFAULT_DIGITS

fibs = FibNum()
for ix,val in enumerate(fibs, 1):
	if len(str(val)) == DIGITS:
		print("Index of first Fibonacci number with {} digits: {}".format(DIGITS, ix))
		break
