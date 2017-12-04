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

# Generate list of four-digit primes
four_digit_primes = list(filter(lambda x: is_prime(x), range(1000, 10_000)))

# Test to see if all values are permutations of one another
def permutations_of_one_another(p, distance):
	nums = sorted(list(str(p)))
	return sorted(list(str(p + distance))) == nums and sorted(list(str(p + distance*2))) == nums

distance = 1
first_prime = None
while first_prime == None:
	distance += 1
	for p in four_digit_primes:
		if (distance != 3330 or p != 1487) and is_prime(p + distance) and is_prime(p + distance*2) and permutations_of_one_another(p, distance):
			first_prime = p
			break

print("Answer: {}{}{}".format(first_prime, first_prime + distance, first_prime + distance*2))
print("Distance: {}".format(distance))
