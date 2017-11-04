#!/usr/bin/python

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def special(n):
  return n == sum([factorials[int(x)] for x in str(n)])

factorials = [factorial(n) for n in range(10)]
result = []
upper_bound = 7 * factorials[9]

for i in range(3, upper_bound):
  if special(i):
    result.append(i)

print("There are {} values satisfying this condition: {}.".format(len(result), ",".join(list(map(str, result)))))
print("Their sum is {}.".format(sum(result)))
