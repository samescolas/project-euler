#!/usr/local/bin/python3

def is_pandigital(n):
	num_str = str(n)
	if len(num_str) == 9 and sorted(num_str) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		return True
	return False

def create_pandigital(seed):
	ret = ""
	multiple = 1
	while len(ret) < 9:
		ret += str(multiple * seed)
		multiple += 1
	if is_pandigital(int(ret)):
		return ret
	return False

max_pandigital = 1

# No need to test anything greater than 10,000 because
# 1*N for N>9,999 would result in a 5-digit number
# (more than half a pandigital)
for i in range(1, 10000):
	num = create_pandigital(i)
	if is_pandigital(num):
		max_pandigital = i

print("{} creates the maximum pandigital value: {}.".format(
	max_pandigital,
	create_pandigital(max_pandigital)
))
