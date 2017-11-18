#!/usr/local/bin/python3

from math import sqrt

# I really should make a prime sieve...
def is_prime(n):
	if n < 0 or (n % 2 == 0 and n > 2):
		return False
	ubound = int(sqrt(n)) + 1
	for i in range(3, ubound, 2):
		if n % i == 0:
			return False
	return True

# Rotate a number one position
def rotate_number(n):
    if n < 10:
        return n
    return int(str(n)[1:] + str(n)[0])

# If number contains a 2 a rotation will be even.
# Otherwise if a number's digits sum to 3 a rotation will be divisible by 3.
# Otherwise test all rotations
def is_circular_prime(n):
    if '2' in str(n) or '0' in str(n) or sum([int(ch) for ch in str(n)]) % 3 == 0:
        return False
    if not is_prime(n):
        return False
    new_number = rotate_number(n)
    while new_number != n:
        if not is_prime(new_number):
            return False
        new_number = rotate_number(new_number)
    return True

# Starting with 2 and 3 to keep the exceptions list
# for is_circular_prime a bit shorter
circular_primes = [2, 3]

# Loop through all odd numbers larger than 4 to test for circular primality
for number in range(5, 1000000, 2):
    if is_circular_prime(number):
        circular_primes.append(number)

print("There are {} circular primes: {}.".format(
    len(circular_primes),
    ",".join([str(n) for n in circular_primes])
))
