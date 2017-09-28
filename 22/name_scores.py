#!/usr/bin/python

import csv

def score_name(name, weight):
	return weight * sum([ord(ch) - 64 for ch in name])

names = []
count = 0
with open('names.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		names = row
		break

name_scores = 0

for i,name in enumerate(sorted(names), 1):
	name_scores += score_name(name, i)

print("Total score: {}".format(name_scores))
