#!/bin/bash                                                     
                                                                                                                                                   
################################################################
################################################################

# BEFORE YOU START CREATE A CMSENV USING THE FOLLOWING COMMANDS:
# source ~/.profile <-- usually not necessary
# cmsrel CMSSW_9_4_6_patch1
# cd CMSSW_9_4_6_patch1/src
# cmsenv
# export CMSSW_BASE=

################################################################
################################################################

# declare states to analyze
#declare -a states=('ttGamma_Dilept_5f_ckm_LO')
#declare -a states=('ttGamma_SingleLeptFromTbar_5f_ckm_LO' 'ttGamma_SingleLeptFromT_5f_ckm_LO' 'ttGammaHadronic_5f_ckm_LO')
declare -a states=('gg_ttGG' 'gg_ttZZ' 'gg_ttZG')

# polynomial order
polyorder='4'

# dim6 operators and stepsize as string
operators='cpQM 1 cpt 1 ctZ 1'

# set reference point
referencepoint='ctZ 4'

# declare number of jets
num_jets=''

# lxplus GRID
lxplus='local'

################################################################

export CMSSW_BASE=
cd `dirname "$0"`

for state in "${states[@]}"
do

   name=$state$num_jets\_rwgt
   carddir=addons/cards/$name/

   # create output dir
   outputpath=$PWD/output/$state/order$polyorder/
   mkdir -p $outputpath

   # create reweight card
   ./make_reweight_card.py --overwrite --filename $PWD/$carddir/$name\_reweight_card.dat --couplings $polyorder $operators --referencepoint $referencepoint

   # create customize card
   ./make_customizecard.py --filename $PWD/$carddir/$name\_customizecards.dat --referencepoint $referencepoint

   # run gridpack generation
   echo "No submission because lxbatch is OFF"
   ./submit_gridpack_generation.sh 30000 30000 $lxplus $name $carddir $lxplus $outputpath
done



