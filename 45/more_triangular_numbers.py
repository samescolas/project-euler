#!/usr/local/bin/python3

from math import sqrt

def is_pentagonal(n):
	if n < 0:
		return False
	test = float(sqrt(24*n + 1) + 1) / 6
	return test - int(test) == 0

def is_hexagonal(n):
	test = float(sqrt(8*n + 1) + 1) / 4
	return test - int(test) == 0

def triangular_number(n):
	return int((n * (n+1))/2)

tri_ix = 285
while True:
	tri_ix += 1
	tri = triangular_number(tri_ix)
	if is_pentagonal(tri) and is_hexagonal(tri):
		break

print("The next triangular number that is also pentagonal and hexagonal is {}.".format(triangular_number(tri_ix)))
