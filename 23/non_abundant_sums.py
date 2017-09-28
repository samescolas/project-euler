#!/usr/bin/python

def get_factors(n):
	factors = []
	for i in xrange(1, int((n / 2) + 1)):
		if n % i == 0:
			factors.append(i)
	return factors

def is_abundant(n):
	if sum(get_factors(n)) > n:
		return True
	return False

print("Obtaining list of abundant numbers...")

# Gather list of all abundant numbers
abundant_numbers = []
for n in xrange(12,28123):
	if is_abundant(n):
		abundant_numbers.append(n)

print("Found {} abundant numbers.".format(len(abundant_numbers)))

# Collect all values that are not the sum of two abundant numbers
non_sums = []
for n in xrange(1,28123):
	is_sum = False
	for potential_summand in list(filter(lambda x: x < n, abundant_numbers)):
		if (n - potential_summand) in abundant_numbers:
			is_sum = True
			break
	if not is_sum:
		non_sums.append(n)

# Print sum
print("Total sum: {}".format(sum(non_sums)))
