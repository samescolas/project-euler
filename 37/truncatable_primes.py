#!/usr/local/bin/python3

from math import sqrt
from functools import reduce

LEFT = 1
RIGHT = 2

def truncate(n, direction):
	num_str = str(n)
	if len(num_str) == 1:
		return None
	if direction == LEFT:
		return int(num_str[1:])
	else:
		return int(num_str[0:-1])

def is_prime(n):
	if n < 2 or (n % 2 == 0 and n > 2):
		return False
	ubound = int(sqrt(n)) + 1
	for i in range(3, ubound, 2):
		if n % i == 0:
			return False
	return True

def is_truncatable_prime(n):
	for direction in [LEFT, RIGHT]:
		num = n
		while num != None:
			if not is_prime(num):
				return False
			else:
				num = truncate(num, direction)
	return True

super_cool_primes = []
search_val = 10

while len(super_cool_primes) != 11:
	if is_truncatable_prime(search_val):
		super_cool_primes.append(search_val)
	search_val += 1

print("Super cool primes: {}.".format(", ".join([str(i) for i in super_cool_primes])))
print("Their sum is {}.".format(reduce(lambda x,y: x+y, super_cool_primes)))
