#!/usr/bin/python

import sys

count = 0
oldKey = None
# Loop around the data
# It will be in the format key/tval
# where key is the website name, val is 1
#
# accmulate the counting for each website name

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# something has gone wrong, skip this line.
		continue

	thisKey = data_mapped[0]

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", count
		oldKey = thisKey
		count = 0

	oldKey = thisKey
	count += 1

if oldKey != None:
	print oldKey, "\t", count 
