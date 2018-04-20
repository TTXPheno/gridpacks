#!/usr/bin/env python

# Standard imports
import argparse
import os
import sys
import itertools

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--couplings',   action='store',         default=[],         nargs='*',  type = str, help="Give a list of the non-zero couplings with values, e.g. NAME1 VALUE1 NAME2 VALUE2")
argParser.add_argument('--filename',    action='store',         default="./reweight_card.dat",  nargs=1,    type = str, help="Output filename")
argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite exisiting x-sec calculation and gridpack")
args = argParser.parse_args()


# recursively make a for loop over all couplings
def recurse( c_list ):
    var, vals = c_list[-1]
    pairs     = [ (var, val) for val in vals ]
    if len(c_list)>1:
        rec       = recurse(c_list[:-1])
        return [ r + p for p in pairs for r in rec] 
    else:
        return pairs

def getWeightName( reweight ):
    name = "_".join( [ ("%s_%8.6f"%( reweight[2*i], reweight[2*i+1] )).rstrip('0') for i in range(len(reweight)/2) ] ) 
    return name.replace('.','p').replace('-','m')

def make_reweight_card( filename, reweights ):
    import datetime
    if not filename.endswith('.dat'):
        raise ValueError( "filename does not end with .dat" )
    with open(filename, "w") as out_file:
        out_file.write("# reweight card file created with https://github.com/schoef/gridpacks on %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        out_file.write("# Command line arguments: "+" ".join(sys.argv)+'\n')
        out_file.write("change rwgt_dir rwgt\n\n")
        out_file.write( "launch --rwgt_name=dummy # Name of first argument seems to be rwgt_1. Add dummy to fix it.\n\n" )
        for reweight in reweights:
            name = getWeightName( reweight )
            out_file.write( "launch --rwgt_name=%s\n"%name )
            name = "_".join( [ ("%s_%8.6f"%( reweight[2*i], reweight[2*i+1] )).rstrip('0') for i in range(len(reweight)/2) ] ) 
            name = name.replace('.','p').replace('-','m')
            for i in range(len(reweight)/2):
                out_file.write("set %s %8.6f\n"%( reweight[2*i], reweight[2*i+1]))
            out_file.write('\n')
    print "Written %i weights to file:"%len(reweights), filename 

def make_reweight_pkl( filename, reweights ):
    import pickle
    pklfilename = filename.replace('.dat','.pkl')
    rw_dict = {}
    for i_reweight, reweight in enumerate(reweights):
        name = getWeightName( reweight )
        #rw_dict[i_reweight] = name 
        rw_dict[name] = i_reweight 
    pickle.dump(rw_dict, file(pklfilename,'w')) 
    print "Written pkl file for enumeration (%i weights):"%len(reweights), pklfilename

def isA( a, type):
    try:
        type(a)
    except ValueError:
        return False
    return True

print "Coupling arguments: %r" % args.couplings

# make a list of the form [ ['c1', v1, v2, ...], ['c2', ...] ] so we can recurse in the couplings c1,c2,... 
coupling_list = []
if len(args.couplings)>0 and isA( args.couplings[0], int ):
    # if 'N_int X a Y b Z c' produce all combinations with replacements up to order N of the form X=n_x*a, Y=n_y*b such that Sum(n_i)<=N
    param_points = []
    order = int(args.couplings[0])
    vars      = args.couplings[1:][::2] 
    stepsize  = map( float, args.couplings[1:][1::2] )
    assert len(vars)==len(stepsize), "Number of variables and number of stepsizes not the same. Got %i and %i, respectively." %( len(vars), len(stepsize))
    for order_ in range(0, order+1):
        for comb in itertools.combinations_with_replacement(range(len(vars)), order_):
            param_point = tuple()
            for i_var, var in enumerate(vars):
                count = comb.count(i_var)
                #if count>0:
                param_point+=(var, count*stepsize[i_var])
            param_points.append( param_point )
elif len(args.couplings)>0:

    # if 'X_string a b c Y e f g Z ...' -> produce all combinations (X=a, Y=e, Z=...) ... (X=c,Y=g,Z=...)
    for a in args.couplings:

        if isA(a, float ):
            val = float(a) 
        else:
            coupling_list.append( [ a, [] ] )
            val = None
        if val is not None: coupling_list[-1][1].append( val )
    param_points = recurse( coupling_list ) if len(coupling_list)>0 else [[]]
else:
    param_points = [[]]

if not os.path.exists( args.filename ) or args.overwrite:
    make_reweight_card( args.filename, param_points )
    make_reweight_pkl( args.filename, param_points )

elif os.path.exists( args.filename ):
    print "Found",args.filename, "do nothing." 
