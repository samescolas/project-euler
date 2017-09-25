#!/usr/bin/python

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n - 1)

print(sum([int(ch) for ch in str(factorial(100))]))
