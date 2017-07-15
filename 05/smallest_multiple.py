import sys
from math import sqrt


def is_prime(n):
    upper_boundary = int(sqrt(n))
    for i in xrange(2, upper_boundary + 1):
        if n % i == 0:
            return False
    return True

def get_prime_factors(n):
    factors = []
    rem = n
    p = 2
    count = 0

    while rem > 1:
        if rem % p == 0:
            count += 1
            rem /= p
        else:
            if count > 0:
                factors.append([p, count])
            p += 1
            while is_prime(p) == False:
                p += 1
            count = 0
    if count > 0:
        factors.append([p, count])


    return factors

primes = {}
for i in xrange(2, int(sys.argv[1]) + 1):
    factors = get_prime_factors(i)
    for (p,n) in factors:
        if p in primes.keys():
            if primes[p][0] < n:
                primes[p][0] = n
            primes[p][1] += n;
        else:
            primes[p] = [n,n]

redundancy = 1
for p in primes.keys():
    redundancy *= pow(p, primes[p][1] - primes[p][0])

print 'min: ' + str(reduce((lambda x,y: x*y), range(2,int(sys.argv[1]) + 1)) / redundancy)
