#!/usr/local/bin/python3

from math import sqrt

def is_pentagonal(n):
	if n < 0:
		return False
	test = float(sqrt(24*n + 1) + 1) / 6
	return test - int(test) == 0

def pentagonal_number(n):
	return n * ((3 * n - 1) / 2)

result = None
for distance in range(1, 100000):
	if result != None:
		break
	for i in range(1, 10000):
		a, b = pentagonal_number(i), pentagonal_number(i + distance)
		if is_pentagonal(a + b) and is_pentagonal(b - a):
			result = int(abs(a - b))
			break

print("The distance between the first two pentagonal numbers with this property is {}.".format(result))
