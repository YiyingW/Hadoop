#!/usr/bin/python

# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET http://www.the-associates.co.uk/assets/js/lowpro.js HTTP/1.1" 200 10469
# %h %l %u %t \"%r\" %>s %b
# we want element %r 
# we need to write them out to standard output, separated by a tab with the integer 1 for the purpose of counting

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		if data[6].startswith('http://www.the-associates.co.uk'):
			s=data[6][31:]
		else:
			s=data[6]

		print "{0}\t{1}".format(s, 1)

