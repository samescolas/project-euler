#!/usr/local/bin/python3

from math import sqrt

# We're searching for the smallest number < 1,000,000
MAX_VAL = 1_000_000

def is_prime(n):
	if n < 2 or (n % 2 == 0 and n > 2):
		return False
	ubound = int(sqrt(n)) + 1
	for i in range(3, ubound, 2):
		if n % i == 0:
			return False
	return True

# find the max number of primes starting with prime[ix] (searching through all indices below) s.t. the
# sum of all consecutive prime values from that one is prime and < MAX_VAL (1,000,000 for ProjectEuler)
def find_max_sum(ix, primes):
	if primes[ix] > MAX_VAL:
		return 0,0
	candidates = [primes[ix]]
	while candidates[-1] < MAX_VAL:
		candidates.append(candidates[-1] + primes[ix+len(candidates)])
	prime_candidates = list(filter(lambda n: n < MAX_VAL and is_prime(n), candidates))
	return candidates.index(prime_candidates[-1]) + 1, prime_candidates[-1]

# generate a list of primes
primes = list(filter(lambda x: is_prime(x), range(1, 100_000)))
max_len, max_val = 0, 0

for start_ix in range(250):
	tmp_max_len, tmp_max_val = find_max_sum(start_ix, primes)
	if tmp_max_len > max_len:
		max_val, max_len = tmp_max_val, tmp_max_len

print("The maximum consecutive sum prime is {} with a length of {}.".format(max_val, max_len))
