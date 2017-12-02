#!/usr/local/bin/python3

def generate_triangle_number(n):
	return 0.5 * n * (n + 1)

def is_triangle_number(n):
	return n in triangle_numbers

# Generate list of triangle numbers
triangle_numbers = [generate_triangle_number(i) for i in range(1000)]

# Read file into sorted list of numbers
with open('./words.txt', 'r') as word_file:
	words = sorted(list(map(lambda w: sum([ord(ch) - 64 for ch in w]), word_file.readlines()[0].replace('"', '').replace('\n', '').split(','))))

# Count words that are triangle numbers
total = 0
for number in words:
	if is_triangle_number(number):
		total += 1

print("There are {} triangle words in this list.".format(total))
