#!/usr/bin/python

import sys

def get_decimal_length(n):
	decimal_val = get_decimal(n)
	return len(decimal_val) if decimal_val is not None else 0

def get_decimal(denominator):
	result = ""
	numerator = 1
	while numerator != 0 and len(result) < denominator * 2:
		numerator *= 10
		result += str(int(numerator/denominator))
		numerator = numerator - int(numerator/denominator) * denominator
	return result if is_repeating(result) else None

def is_repeating(num_str):
	if len(num_str) % 2 == 1 or len(num_str) <= 1:
		return False
	print("Comparing {} and {}".format(num_str[:int(len(num_str)/2)],num_str[int(len(num_str)/2):]))
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

print("\n\n\n\n\n1/{} = 0.{} has the longest repeating decimal ({}) under {}.".format(
	max_i, get_decimal(max_i), max/2, UPPER_BOUND))


print("1/{} = 0.{}".format(UPPER_BOUND, get_decimal(UPPER_BOUND)))
