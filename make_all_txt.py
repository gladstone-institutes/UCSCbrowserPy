#!/usr/local/bin/python

import os
import sys, getopt

# Get full command-line arguments
full_cmd_arguments = sys.argv

# Keep all but the first
argument_list = full_cmd_arguments[1:]
print("\n\n\nUSAGE: python make_all_txt.py <bigWigDir> <bigWigFileExtensio> <outDir> <wynGB_dirName>")
print("EXAMPLE: python make_all_txt.py ./ .bw ./ kchoudha/ppg-Cardiac-KC/\n\n\n")

if (len(argument_list) < 4):
	print('\n\nERROR: Required arguments missing from command line input.')
	sys.exit()

files = os.listdir(argument_list[0])
files = [x for x in files if x.endswith(argument_list[1])]

with open(argument_list[2] + "all.txt", 'w') as outfile:
	outfile.write('## Paste this link into the Genome Browser custom track box: http://wyngb.gladstone.org/data/' + argument_list[3] + 'all.txt' + '\n' + \
		'## Remember to set the default track location to an area with data (e.g. "Gapdh" for human, "Actn1" for mouse)' + '\n' + \
		'## Finally, in the Genome Browser, go to My Data --> Session --> Save Session and save it as (for example): browserTracks_by_Krishna_Choudhary' + '\n\n\n')
	
	for f in files:
		f_name = os.path.basename(f)
		outfile.write("".join(["track type=bigWig name=\"", \
			os.path.splitext(f_name)[0], " (wig)\" description=\"", \
			os.path.splitext(f_name)[0], " (wig)\" bigDataUrl=\"http://wyngb.gladstone.org/data/" + argument_list[3], f_name, "\" alwaysZero=\"on\" visibility=\"full\" color=\"255,0,0\" maxHeightPixels=\"128:32:8\""]))
		outfile.write("\n\n")

