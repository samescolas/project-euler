#!/usr/local/bin/python3

from math import sqrt, ceil

# returns first factor if not prime or 1 otherwise
# by checking all values up to the sqrt of the value
def min_factor(x):
    for i in range(2,int(ceil(sqrt(x)) + 1)):
        if x % i == 0:
            return i
    return 1

def is_prime(n):
	if n < 2 or (n % 2 == 0 and n > 2):
		return False
	ubound = int(sqrt(n)) + 1
	for i in range(3, ubound, 2):
		if n % i == 0:
			return False
	return True

def add(key, d):
	if key in d:
		d[key] += 1
	else:
		d[key] = 1
	return d

def prime_factors(n):
	rem = n
	factors = {}
	while not is_prime(rem):
		factor = min_factor(rem)
		factors = add(factor, factors)
		rem = int(rem / factor)
	if rem > 1:
		return add(rem, factors)
	return factors

def repeats(f1, f2):
	for k in f1.keys():
		if k in f2 and f1[k] == f2[k]:
			return True
	return False

found = False
to_find = 4
n1 = 2
while not found:
	distinct_factors = {}
	for num in range(to_find):
		factors = prime_factors(n1 + num)
		if len(factors) != to_find or repeats(factors, distinct_factors):
			break
		else:
			for k in factors.keys():
				distinct_factors = add("{}^{}".format(k, factors[k]), distinct_factors)
	if len(distinct_factors) == pow(to_find, 2):
		found = True
	else:
		n1 += 1
		distinct_factors = {}

print("Methinks the answer is {}.".format(", ".join([str(i) for i in range(n1, n1 + to_find)])))
for k in distinct_factors.keys():
	print(k)
