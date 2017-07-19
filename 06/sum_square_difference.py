import sys

if len(sys.argv) > 1:
	print reduce((lambda x,y: x+y), [(x**2)*(x-1) for x in xrange(int(sys.argv[1])+1)])
