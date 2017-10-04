#!/usr/bin/python

def bs_reduction(numerator, denominator):
	num = [ch for ch in str(numerator)]
	if ('0' in str(numerator) and '0' in str(denominator)) or numerator == denominator or len(num) != 2 or len(str(denominator)) != 2:# or num[0] not in str(denominator) or num[1] not in str(denominator):
		return False
	for i in range(2):

		try:
			new_numerator = int(str(numerator).replace(num[i], ''))
			new_denominator = int(str(denominator).replace(num[i], ''))
		except:
			return False

		if new_denominator == 0 or denominator == 0:
			return False

		if float(new_numerator)/new_denominator == float(numerator)/denominator:
			return True
	return False

results = set()
for a in range(100):
	for b in range(a):
		if bs_reduction(a, b):
			results.add((a, b))
			print("bs found! {} / {}".format(a, b))
		else:
			print("No bs.")

numerator = 1
denominator = 1
for val in results:
	denominator *= val[0]
	numerator *= val[1]

print("{}/{}".format(numerator, denominator))
