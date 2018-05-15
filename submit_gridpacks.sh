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
declare -a states=('ttZ' 'ttgamma' 'ttW')

# polynomial order
polyorder='3'

# dim6 operators and stepsize as string
operators='ctp 1 ctpI 1 cpQM 1 cpQ3 1 cpt 1 cptb 1 cptbI 1 ctW 1 ctWI 1 ctZ 1 ctZI 1 cbW 1 cbWI 1 ctG 1 ctGI 1'

# set reference point
referencepoint='ctW 4 ctWI 4 ctZ 4 ctZI 4 ctG 4 ctGI 4'

# declare number of jets
num_jets='0j'

# lxplus GRID
lxplus='2nw'

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
   ./make_reweight_card.py --overwrite --filename $PWD/$carddir/$name\_reweight_card.dat  --referencepoint $referencepoint --couplings $polyorder $operators

   # create customize card
   ./make_customizecard.py --filename $PWD/$carddir/$name\_customizecards.dat --referencepoint $referencepoint

   # run gridpack generation
   ./submit_gridpack_generation.sh 30000 30000 $lxplus $name $carddir $lxplus $outputpath

done



