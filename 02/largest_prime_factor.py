import sys
from math import sqrt,ceil

# returns first factor if not prime or 1 otherwise
# by checking all values up to the sqrt of the value
def min_factor(x):
    for i in range(2,int(ceil(sqrt(x)) + 1)):
        if x % i == 0:
            return i
    return 1

# a function to make things less ugly
def is_prime(x):
    if min_factor(x) == 1:
        return True
    return False

input_val = long(sys.argv[1])

# divide input value by min factor until its prime
guess = input_val / min_factor(input_val)
while True:
    if is_prime(guess):
        print guess
        break
    guess = guess / min_factor(guess)
