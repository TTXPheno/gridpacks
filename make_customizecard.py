#!/usr/bin/env python

# Standard imports
import argparse
import os
import sys
import itertools

# generate the customizecard
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--referencepoint',   action='store',         default=[],         nargs='*',  type = str, help="Give a list of the non-zero WC with values as a reference point, e.g. NAME1 VALUE1 NAME2 VALUE2 ...")
argParser.add_argument('--filename',    action='store',         default="./customize_card.dat",  nargs=1,    type = str, help="Output filename")
argParser.add_argument('--append',   action='store_true',    help="Overwrite exisiting x-sec calculation and gridpack")
args = argParser.parse_args()


def make_customize_card(filename, referencepoint, append=False):
    import datetime
    if not filename.endswith('.dat'):
        raise ValueError( "filename does not end with .dat" )
    if not append:
        with open(filename, "w") as out_file:
            out_file.write("# customize card file created with https://github.com/TTXPheno/gridpacks on %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            out_file.write("# Command line arguments: "+" ".join(sys.argv)+'\n')
            out_file.write("# Reference Point: "+" ".join(referencepoint)+'\n')
            out_file.write("set param_card mass 6 172.5\n")
	    out_file.write("set param_card mass 25 125.0\n")
            out_file.write("set param_card yukawa 6 172.5\n")
            out_file.write("set param_card decay 6 auto\n")
    with open(filename, "a") as out_file:
        for i in range(0, len(referencepoint), 2):
            out_file.write("set param_card %s %8.6f\n" %( referencepoint[i], float(referencepoint[i+1])))

    print "Written %i weights to file:"%int(len(referencepoint)/2), filename


if type(args.filename) == list: args.filename = args.filename[0]
make_customize_card(args.filename, args.referencepoint, args.append)
