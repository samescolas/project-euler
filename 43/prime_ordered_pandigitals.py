#!/usr/local/bin/python3

from itertools import permutations

def contains_prime_things(n):
	primes = [2, 3, 5, 7, 11, 13, 17]
	for ix, p in enumerate(primes):
		if int(n[ix+1:ix+4]) % p != 0:
			return False
	return True

total = 0
for permutation in permutations("1023456789"):
	if contains_prime_things("".join(permutation)):
		total += int("".join(permutation))

print("The total of all pandigitals with this property is {}.".format(total))
