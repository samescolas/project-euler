#!/usr/local/bin/python3

def count_consecutive_twins(n):
	count = 1
	check = sorted(list(str(n)))
	val = n*2
	while sorted(list(str(val))) == check:
		val += n
		count += 1
	return count

def main():
	search_val = 1
	while count_consecutive_twins(search_val) != 6:
		# If 6*N has more digits than N, skip to smallest number with one more digit than N.
		if len(str(search_val * 6)) > len(str(search_val)):
			search_val = int("1"+"0"*len(str(search_val)))
		else:
			search_val += 1
	print("The first number s.t. 1x, 2x, ..., 6x all contain the same digits is {}.".format(search_val))

if __name__ == '__main__':
	main()
