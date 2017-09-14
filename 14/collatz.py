import sys

# Decorator function to add static variable to count_chain function
def static_vars(**kwargs):
	def decorate(func):
		for k in kwargs:
			setattr(func, k, kwargs[k])
		return func
	return decorate

def get_next_value(n):
	if n == 1:
		return n
	elif n % 2 == 0:
		return int(n / 2)
	return 3 * n + 1

# Dynamic programming, I think? Store known values to save time calculating.
@static_vars(hist={})
def count_chain(n):
	count = 1
	while (n != 1):
		count += 1
		if n in count_chain.hist:
			return count + count_chain.hist[n]
		n = get_next_value(n)
	count_chain.hist[n] = count
	return count

if len(sys.argv) > 1:	
	search_val = int(sys.argv[1])
else:
	search_val = 1000000

n = 1
max = count_chain(n)
count = count_chain(n)
max_n = n
while n < search_val:
	print(n, ':', max_n, ':', max, ':', count)
	count = count_chain(n)
	if count > max:
		max = count
		max_n = n
	n += 1
print(max_n, ':', max)
