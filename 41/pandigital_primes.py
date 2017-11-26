#!/usr/local/bin/python3

from math import sqrt
from itertools import permutations

def is_prime(n):
	if n < 2 or (n % 2 == 0 and n > 2):
		return False
	ubound = int(sqrt(n)) + 1
	for i in range(3, ubound, 2):
		if n % i == 0:
			return False
	return True

def create_pandigital(num_digits):
	ret = ""
	for digit in range(num_digits, 0, -1):
		ret += str(digit)
	return ret

found = False

for digits in range(9, 0, -1):
	for permutation in permutations(create_pandigital(digits)):
		if is_prime(int("".join(permutation))):
			print("The largest prime pandigital number is {}!".format("".join(permutation)))
			found = True
			break
	if found:
		break
