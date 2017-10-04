#!/usr/bin/python

import sys

DEFAULT = 200

try:
	TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT

except:
	TARGET = DEFAULT

def count(S, m, n):
	table = [[0 for x in range(m)] for x in range(n + 1)]

	for i in range(m):
		table[0][i] = 1

	for i in range(1, n+1):
		for j in range(m):
			x = table[i - S[j]][j] if i - S[j] >= 0 else 0
			y = table[i][j - 1] if j >= 1 else 0
			table[i][j] = x + y
	
	return table[n][m-1]


coins = [1, 2, 5, 10, 20, 50, 100, 200]

print("There are %d ways to make change for $%d.%02d" % (count(coins, len(coins), TARGET), int(TARGET/100), TARGET%100))
