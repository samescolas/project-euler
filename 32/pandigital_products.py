#!/usr/bin/python

def is_pandigital(n):
	n = str(n)
	return len(n) == 9 and not '123456789'[:9].strip(n)

result = {}
for i in range(2, 60):
	start = 123 if len(str(i * 1234)) > 4 else 1234
	for j in range(start, 10000/i):
		if is_pandigital(str(i) + str(j) + str(i*j)):
			if i*j not in result:
				result[i*j] = True

print("Sum of products: %d"%sum(result.keys()))
