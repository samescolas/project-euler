#!/usr/bin/python

from math import pow

def f(a, b):
	return pow(a, b)

result = {}

for a in range(2, 101):
	for b in range(2, 101):
		val = f(a, b)
		if val not in result:
			result[val] = 1
		else:
			result[val] += 1

print("There are {} distinct values.".format(len(result)))
