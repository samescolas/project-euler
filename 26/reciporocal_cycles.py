#!/usr/bin/python

import sys

def get_decimal_length(n):
	decimal_val = get_decimal(n)
	return len(decimal_val) if decimal_val is not None else 0

def get_decimal(denominator):
	result = []
	numerator = 1
	while numerator != 0 and len(result) < denominator:
		numerator *= 10
		result.append(int(numerator/denominator))
		numerator = numerator - int(numerator/denominator) * denominator
	return result if numerator == 0 else None

def is_repeating(n):
	num_str = str(n)
	if len(num_str) % 2 == 1:
		return False
	return (num_str[:int(len(num_str)/2)] == num_str[int(len(num_str)/2):])

DEFAULT = 1000

try :
	UPPER_BOUND = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT

except:
	UPPER_BOUND = DEFAULT

max = 1
max_i = 1
for i in xrange(1,1000):
	val = get_decimal_length(i)
	if val is not None and val > max:
		max = val
		max_i = i

print("1/{} = 0.{} has the longest repeating decimal ({}) under {}.".format(
	max_i, "".join(map(lambda x: str(x), get_decimal(max_i))), max, UPPER_BOUND))
