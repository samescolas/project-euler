#!/usr/local/bin/python3

def champernownes_constant(seed):
	ret = ""
	for i in range(pow(10, seed), pow(10, seed + 1)):
		ret += str(i)
	return ret

# List of decimal places we are interested in
places = [pow(10, n) for n in range(7)]

# Index starts at 1
range_start = 1

# Generate the first piece of the list (0.123456789)
champernowne = champernownes_constant(0)

# Set seed to 1 to generate next part of list
seed = 1

# Answer is a product so we will start at 1
answer = 1

# For each decimal place we are interested in
for position in places:
	# If value is within currencly generated piece of constant
	if range_start <= position < range_start+len(champernowne):
		# Add value to solution
		answer *= int(champernowne[position - range_start])
	else:
		# Otherwise generate next piece of constant and update values
		range_start += len(champernowne)
		champernowne = champernownes_constant(seed)
		seed += 1
		answer *= int(champernowne[position - range_start])

print("Product: {}".format(answer))
