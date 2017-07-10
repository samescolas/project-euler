import sys

print (reduce((lambda x, y: x + y), map((lambda x: x if x % 3 == 0 or x % 5 == 0 else 0), range(int(sys.argv[1])))));
