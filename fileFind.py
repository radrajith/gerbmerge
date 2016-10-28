import glob
import os
from os.path import isfile, join

a = raw_input("SubString: ")
os.chdir("C:\\Users\\xxxx\\Senior Fall 2016\\ESE 323\\gerbmerge\\alltextfiles")
for filename in glob.glob("*.txt"):
	if isfile(filename):
		f = open(filename, 'r')
		for line in f:
			if(line.find(a) > 0):
				print filename
				break;