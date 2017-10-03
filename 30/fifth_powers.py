#!/usr/bin/python

from math import pow

def special(n):
	return n == sum([pow(int(ch), 5) for ch in str(n)])

result = []

for i in range(2, 1000000):
	if special(i):
		result.append(i)

print("There are {} values satisfying this condition: {}.".format(len(result), ",".join(list(map(str, result)))))
print("Their sum is {}.".format(sum(result)))
