#!/usr/local/bin/python3

import sys
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

# Returns the number of primes and the first prime in the given family
def count_primes_in_family(n):
	count = 0
	smallest = None
	if n[0] == '*':
		for replacement_digit in range(1, 10):
			if is_prime(int(n.replace('*', str(replacement_digit)))):
				count += 1
				if smallest == None:
					smallest = int(n.replace('*', str(replacement_digit)))
	else:
		for replacement_digit in range(10):
			if is_prime(int(n.replace('*', str(replacement_digit)))):
				count += 1
				if smallest == None:
					smallest = int(n.replace('*', str(replacement_digit)))
	return count, smallest

# Searches all permutations of set of values
# Ie. (n=123, replacements=1) => { *123, 1*23, 12*3, 123* }
def find_n_digit_prime_family(n, replacements):
	for permutation in permutations(str(n) + "*"*replacements):
		if permutation[0] == '0':
			continue
		num_str = "".join(permutation)
		count, answer = count_primes_in_family(num_str)
		if count == SEARCH_VAL:
			return permutation, answer
	return None

try:
	SEARCH_VAL = int(sys.argv[1])

except:
	SEARCH_VAL = 8

def main():
	num_digits = 1
	answer = None
	while answer == None:
		num_digits += 1
		for num_replacements in range(num_digits - 1, 0, -1):
			l_bound = int("1" + "0"*(num_digits - num_replacements - 2))
			if num_digits - num_replacements - 1 > 0:
				l_bound = int(str(l_bound) + "1")
			u_bound = int("9"*(num_digits - num_replacements)) + 1
			for n in range(l_bound, u_bound):
				answer = find_n_digit_prime_family(n, num_replacements)
				if answer != None:
					break
			if answer != None:
				break

	print("{} of the family {} is the smallest prime of the first {}-digit family.".format(answer[1], "".join(answer[0]), SEARCH_VAL))

if __name__ == '__main__':
	main()
