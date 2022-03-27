#!/usr/bin/env python
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA') #Description
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") #After -s add the input sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") #After -m add the Motif you are looking at

if len(sys.argv) == 1:
	parser.print_help()
	sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()


if re.search('^[ACGTU]+$', args.seq):
	if re.search('T', args.seq):
		print ('The sequence is DNA') #If it finds a T, it will be DNA
	elif re.search('U', args.seq):
		print ('The sequence is RNA') #If it finds a U, it will be RNA
	else:
		print ('The sequence can be DNA or RNA') #In other situations it can be both
else:
	print ('The sequence is not DNA nor RNA') #It prints a message for those sequences which are not defined as DNA or RNA.

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("The motif has been found") #Message that is going to retrieve if it finds the motif
    else:
        print("The motif has not been found") #Message that is not going to retrieve if it does not find the motif


