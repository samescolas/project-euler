#!/usr/local/bin/python3

from math import sqrt

def is_prime(n):
	if n < 2 or (n % 2 == 0 and n > 2):
		return False
	ubound = int(sqrt(n)) + 1
	for i in range(3, ubound, 2):
		if n % i == 0:
			return False
	return True

# Assume first counterexample is less than 100,000
primes = list(filter(lambda x: is_prime(x), range(1, 100_000)))

result = None
found_p_and_sq = False
n = 1
# Loop through odd numbers
while result == None:
	n += 2
	for p in primes:
		sq = 0
		if found_p_and_sq:
			break
		while (2 * pow(sq, 2)) + p <= n:
			if (2 * pow(sq, 2)) + p == n:
				print("[{}] = 2*{}^2+{}".format(n, sq, p))
				found_p_and_sq = True
				break
			sq += 1
	if found_p_and_sq:
		found_p_and_sq = False
	else:
		result = n

print("{} breaks Goldbach's conjecture.".format(result))
