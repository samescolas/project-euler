import sys

count = 0
p = 2
while count < int(sys.argv[1]):
    if all (p % y != 0 for y in xrange(2, p)):
        count += 1
    if count == int(sys.argv[1]):
        print p
        break
    p += 1
