import sys

class FibNum:
	def __init__(self, max):
		self.max = max

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def next(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib

print reduce((lambda x, y: x + y), filter(lambda x: x % 2 == 0, FibNum(long(sys.argv[1]))))
