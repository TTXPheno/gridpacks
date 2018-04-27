# gridpacks
Repository for generating gridpacks with reweighting with amcatnlo 

Card templates can be found in the path addons/cards/UFOMODEL_template and the corresponding UFO file in addons/models
to generate a gridpack run "source submit_madpack_ttbareft.sh"
this will copy the template and replace settings in the default templates if needded according to what is specified 
in the submit script 
modify customize card to change the corresponding operators you want to use
the example gridpack gluontop_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz was tested in debug which 
also contains an example lhe output with EFT and systematics weights   


## Generate multiple gridpacks
To generate more than one gridpack use submit_gridpacks.sh

Before you start create a cms environment using the following commands:
source ~/.profile <-- usually not necessary (to define the aliases)
cmsrel CMSSW_9_4_6_patch1
cd CMSSW_9_4_6_patch1/src
cmsenv
export CMSSW_BASE=

Define the following parameters in submit_gridpacks.sh:
Output directory
states to analyze (e.g. ttZ ttgamma) <-- make sure you have all cards in addons/cards/
declare number of jets
declare polynomial order (e.g. 2nd, 3rd, 4th)
lxplus GRID (where to calculate)
dim6 operators and stepsize as string (e.g. 'ctZ 1 ctZI 1')

The script will loop over all polynomial orders and all states to analyze and create a directory structure in the output directory containing the calculated gridpacks
