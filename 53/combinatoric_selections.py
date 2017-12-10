#!/usr/local/bin/python3

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n - 1)

def n_choose_r(n, r):
	return int(factorial(n) / (factorial(r) * factorial(n - r)))

def count_vals_above_million(n):
	count = 0
	prev = None
	for r in range(n):
		curr = n_choose_r(n, r)
		if curr > 1_000_000:
			count += 1
		if prev != None and prev > curr and curr < 1_000_000:
			break
		prev = curr
	return count

count = 0
for n in range(101):
	count += count_vals_above_million(n)

print("There are {} values of nCr greater than 1,000,000 for 1<=n<=100.".format(count))
