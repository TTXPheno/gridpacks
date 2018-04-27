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

# Output directory
outputdir='../gridpacks_data'

# declare states to analyze
declare -a states=('ttZ' 'ttgamma' 'ttW')

# declare number of jets
num_jets='0j'

# declare polynomial order
declare -a polyorders=(2 3)

# lxplus GRID
lxplus='2nw'

# dim6 operators and stepsize as string <-- improve input later
operators='ctZ 1 ctZI 1'

# file addons
reweight_addon='_rwgt'
card_addon='_reweight_card.dat'

################################################################

mkdir -p $outputdir
cd $outputdir

# run all polynomial orders
for polyorder in "${polyorders[@]}"
do
   mkdir order_$polyorder
   cd order_$polyorder

   # run all states
   for state in "${states[@]}"
   do
      mkdir gridpacks_$state
      cd gridpacks_$state

#      git clone https://github.com/TTXPheno/gridpacks.git

      cp -rf ../../../gridpacks/* ./

      # create reweight card
      python make_reweight_card.py --overwrite --couplings $polyorder $operators

      filename=$state$num_jets$reweight_addon$card_addon
      dirname=$state$num_jets$reweight_addon
      fullpath=addons/cards/$dirname/

      mv reweight_card.dat $fullpath/$filename

      # submit job to lxplus
#      ./submit_gridpack_generation.sh 30000 30000 $lxplus $dirname $fullpath $lxplus

      cd ..
   done

   cd ..
done
