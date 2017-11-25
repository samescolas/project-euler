#!/usr/local/bin/python3

from functools import reduce

def binary(n):
	return int(bin(n).lstrip('-0b'))

def is_palindrome(n):
	num_str = str(n)
	num_len = len(num_str)
	for ix,ch in enumerate(num_str):
		if ix >= num_len / 2:
			break
		if num_str[num_len - ix - 1] != ch:
			return False
	return True

double_palindromes = []

for i in range(1, 1000000):
	if is_palindrome(i) and is_palindrome(binary(i)):
		double_palindromes.append(i)

print("There are {} double palindromes with a total sum of {}.".format(
	len(double_palindromes),
	reduce(lambda x,y: x+y, double_palindromes)
))
