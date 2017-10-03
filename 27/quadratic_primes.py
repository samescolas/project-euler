#!/usr/bin/python

from math import sqrt,pow

def is_prime(n):
	if n < 0 or (n % 2 == 0 and n > 2):
		return False
	ubound = int(sqrt(n)) + 1
	for i in range(3, ubound, 2):
		if n % i == 0:
			return False
	return True

def get_primes(a, b):
	def f(n, a, b):
		return pow(n, 2) + a*n + b

	result = []
	n = 0
	value = f(n, a, b)
	while is_prime(value):
		result.append(value)
		n += 1
		value = f(n, a, b)
	return result

max_val = None
max = None
primes = {}
for a in range(-1001, 1000):
	for b in range(-1002, 1001):
		primes[(a,b)] = get_primes(a, b)
		if len(primes[(a,b)]) > max_val or max_val is None:
			max_val = len(primes[(a, b)])
			max = [a, b]

print("n**2 + {}n + {} produces {} consecutive primes.".format(max[0], max[1], max_val))
