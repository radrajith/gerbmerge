import glob
import os
from os.path import isfile, join

a = raw_input("SubString: ")
dir = os.getcwd()
for filename in glob.glob("*.txt"):
	if isfile(filename):
		f = open(filename, 'r')
		for line in f:
			if(line.find(a) > 0):
				print filename
				break;
